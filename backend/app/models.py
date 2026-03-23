from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String(64), index=True)
    model: Mapped[str] = mapped_column(String(64), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    mileage: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float, index=True)
    average_price: Mapped[float] = mapped_column(Float)
    deviation_percent: Mapped[float] = mapped_column(Float, index=True)
    status: Mapped[str] = mapped_column(String(32), index=True)
    region: Mapped[str] = mapped_column(String(64), index=True)
    source_name: Mapped[str] = mapped_column(String(64), default="bankruptcy_feed")
    url: Mapped[str] = mapped_column(String(255), unique=True)
    image_url: Mapped[str] = mapped_column(String(255))
    premium_only: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    comparables: Mapped[list[MarketComparable]] = relationship(back_populates="car", cascade="all, delete-orphan")
    favorites: Mapped[list[Favorite]] = relationship(back_populates="car", cascade="all, delete-orphan")


class MarketComparable(Base):
    __tablename__ = "market_comparables"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id", ondelete="CASCADE"), index=True)
    source_name: Mapped[str] = mapped_column(String(64), default="classifieds_feed")
    title: Mapped[str] = mapped_column(String(255))
    year: Mapped[int] = mapped_column(Integer)
    mileage: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float, index=True)
    url: Mapped[str] = mapped_column(String(255))

    car: Mapped[Car] = relationship(back_populates="comparables")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    premium: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    favorites: Mapped[list[Favorite]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Favorite(Base):
    __tablename__ = "favorites"
    __table_args__ = (UniqueConstraint("user_id", "car_id", name="uq_favorites_user_car"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id", ondelete="CASCADE"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped[User] = relationship(back_populates="favorites")
    car: Mapped[Car] = relationship(back_populates="favorites")
