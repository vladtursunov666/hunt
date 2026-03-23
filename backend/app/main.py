from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from .database import Base, engine, get_db
from .models import Car, Favorite, MarketComparable, User
from .schemas import CarDetailOut, CarsResponse, FavoriteCarOut, FavoriteIn
from .services.seed_data import build_seed_cars


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    with Session(engine) as db:
        has_cars = db.scalar(select(Car.id).limit(1))
        if not has_cars:
            for item in build_seed_cars():
                comparables = item.pop("comparables")
                car = Car(**item)
                for comp in comparables:
                    car.comparables.append(MarketComparable(**comp))
                db.add(car)
            db.commit()
    yield


app = FastAPI(title="Hunt Auto Analytics MVP", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/cars", response_model=CarsResponse)
def list_cars(
    price_min: float | None = None,
    price_max: float | None = None,
    brand: str | None = None,
    year: int | None = None,
    region: str | None = None,
    deviation_min: float | None = Query(default=None),
    deviation_max: float | None = Query(default=None),
    only_free: bool = False,
    db: Session = Depends(get_db),
) -> CarsResponse:
    query = select(Car).order_by(Car.deviation_percent.asc())

    if price_min is not None:
        query = query.where(Car.price >= price_min)
    if price_max is not None:
        query = query.where(Car.price <= price_max)
    if brand:
        query = query.where(Car.brand.ilike(f"%{brand}%"))
    if year:
        query = query.where(Car.year == year)
    if region:
        query = query.where(Car.region.ilike(f"%{region}%"))
    if deviation_min is not None:
        query = query.where(Car.deviation_percent >= deviation_min)
    if deviation_max is not None:
        query = query.where(Car.deviation_percent <= deviation_max)
    if only_free:
        query = query.where(Car.premium_only.is_(False))

    items = list(db.scalars(query).all())
    return CarsResponse(items=items, total=len(items))


@app.get("/cars/{car_id}", response_model=CarDetailOut)
def get_car(car_id: int, db: Session = Depends(get_db)) -> Car:
    car = db.scalar(select(Car).options(selectinload(Car.comparables)).where(Car.id == car_id))
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@app.post("/favorite")
def add_favorite(payload: FavoriteIn, db: Session = Depends(get_db)) -> dict[str, int | str]:
    car = db.get(Car, payload.car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    user = db.scalar(select(User).where(User.telegram_id == payload.telegram_id))
    if not user:
        user = User(telegram_id=payload.telegram_id)
        db.add(user)
        db.flush()

    existing = db.scalar(select(Favorite).where(Favorite.user_id == user.id, Favorite.car_id == payload.car_id))
    if existing:
        return {"status": "exists", "favorite_id": existing.id}

    favorite = Favorite(user_id=user.id, car_id=payload.car_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return {"status": "created", "favorite_id": favorite.id}


@app.get("/users/{telegram_id}/favorites", response_model=list[FavoriteCarOut])
def list_favorites(telegram_id: int, db: Session = Depends(get_db)) -> list[Favorite]:
    user = db.scalar(select(User).where(User.telegram_id == telegram_id))
    if not user:
        return []

    query = (
        select(Favorite)
        .options(selectinload(Favorite.car))
        .where(Favorite.user_id == user.id)
        .order_by(Favorite.created_at.desc())
    )
    return list(db.scalars(query).all())
