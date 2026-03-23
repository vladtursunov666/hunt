import os

os.environ["DATABASE_URL"] = "sqlite:///./test_hunt.db"

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_list_cars_and_filtering():
    response = client.get("/cars")
    assert response.status_code == 200
    payload = response.json()
    assert payload["total"] >= 3

    filtered = client.get("/cars", params={"brand": "Toyota", "only_free": True})
    assert filtered.status_code == 200
    items = filtered.json()["items"]
    assert items
    assert all(item["brand"] == "Toyota" for item in items)
    assert all(item["premium_only"] is False for item in items)


def test_get_car_and_favorite_flow():
    cars = client.get("/cars").json()["items"]
    car_id = cars[0]["id"]

    detail = client.get(f"/cars/{car_id}")
    assert detail.status_code == 200
    assert len(detail.json()["comparables"]) >= 10

    favorite = client.post("/favorite", json={"telegram_id": 123456, "car_id": car_id})
    assert favorite.status_code == 200
    assert favorite.json()["status"] in {"created", "exists"}

    favorites = client.get("/users/123456/favorites")
    assert favorites.status_code == 200
    assert favorites.json()
