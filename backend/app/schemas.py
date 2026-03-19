from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ComparableOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    source_name: str
    title: str
    year: int
    mileage: int
    price: float
    url: str


class CarCardOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    brand: str
    model: str
    year: int
    mileage: int
    price: float
    average_price: float
    deviation_percent: float
    status: str
    region: str
    url: str
    image_url: str
    premium_only: bool
    created_at: datetime


class CarDetailOut(CarCardOut):
    source_name: str
    comparables: list[ComparableOut]


class CarsResponse(BaseModel):
    items: list[CarCardOut]
    total: int


class FavoriteIn(BaseModel):
    telegram_id: int
    car_id: int


class FavoriteOut(BaseModel):
    id: int
    telegram_id: int
    car_id: int
    created_at: datetime


class FavoriteCarOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    car: CarCardOut
    created_at: datetime
