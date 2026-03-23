from __future__ import annotations

from .analytics import calculate_average_price, calculate_deviation_percent, classify_deviation

SEED_CARS = [
    {
        "brand": "Toyota",
        "model": "Camry",
        "year": 2019,
        "mileage": 91000,
        "price": 1520000,
        "region": "Москва",
        "url": "https://bankrot.example/lots/camry-2019-1",
        "image_url": "https://images.unsplash.com/photo-1550355291-bbee04a92027?auto=format&fit=crop&w=900&q=80",
        "premium_only": False,
        "comparables": [
            {"title": "Toyota Camry 2019", "year": 2019, "mileage": 85000, "price": 1920000, "url": "https://market.example/camry-1"},
            {"title": "Toyota Camry 2020", "year": 2020, "mileage": 93000, "price": 1990000, "url": "https://market.example/camry-2"},
            {"title": "Toyota Camry 2018", "year": 2018, "mileage": 98000, "price": 1830000, "url": "https://market.example/camry-3"},
            {"title": "Toyota Camry 2019", "year": 2019, "mileage": 87000, "price": 1950000, "url": "https://market.example/camry-4"},
            {"title": "Toyota Camry 2019", "year": 2019, "mileage": 91000, "price": 1890000, "url": "https://market.example/camry-5"},
            {"title": "Toyota Camry 2018", "year": 2018, "mileage": 102000, "price": 1780000, "url": "https://market.example/camry-6"},
            {"title": "Toyota Camry 2021", "year": 2021, "mileage": 70000, "price": 2100000, "url": "https://market.example/camry-7"},
            {"title": "Toyota Camry 2019", "year": 2019, "mileage": 95000, "price": 1870000, "url": "https://market.example/camry-8"},
            {"title": "Toyota Camry 2017", "year": 2017, "mileage": 120000, "price": 1700000, "url": "https://market.example/camry-9"},
            {"title": "Toyota Camry 2019", "year": 2019, "mileage": 88000, "price": 1945000, "url": "https://market.example/camry-10"},
        ],
    },
    {
        "brand": "BMW",
        "model": "X5",
        "year": 2018,
        "mileage": 120000,
        "price": 2850000,
        "region": "Санкт-Петербург",
        "url": "https://bankrot.example/lots/bmw-x5-2018-1",
        "image_url": "https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=900&q=80",
        "premium_only": True,
        "comparables": [
            {"title": "BMW X5 2018", "year": 2018, "mileage": 114000, "price": 3300000, "url": "https://market.example/x5-1"},
            {"title": "BMW X5 2019", "year": 2019, "mileage": 105000, "price": 3690000, "url": "https://market.example/x5-2"},
            {"title": "BMW X5 2017", "year": 2017, "mileage": 128000, "price": 3100000, "url": "https://market.example/x5-3"},
            {"title": "BMW X5 2018", "year": 2018, "mileage": 121000, "price": 3250000, "url": "https://market.example/x5-4"},
            {"title": "BMW X5 2020", "year": 2020, "mileage": 98000, "price": 3850000, "url": "https://market.example/x5-5"},
            {"title": "BMW X5 2018", "year": 2018, "mileage": 125000, "price": 3150000, "url": "https://market.example/x5-6"},
            {"title": "BMW X5 2017", "year": 2017, "mileage": 133000, "price": 3050000, "url": "https://market.example/x5-7"},
            {"title": "BMW X5 2018", "year": 2018, "mileage": 119000, "price": 3220000, "url": "https://market.example/x5-8"},
            {"title": "BMW X5 2019", "year": 2019, "mileage": 101000, "price": 3520000, "url": "https://market.example/x5-9"},
            {"title": "BMW X5 2018", "year": 2018, "mileage": 117000, "price": 3180000, "url": "https://market.example/x5-10"},
        ],
    },
    {
        "brand": "Lada",
        "model": "Vesta",
        "year": 2021,
        "mileage": 47000,
        "price": 880000,
        "region": "Татарстан",
        "url": "https://bankrot.example/lots/vesta-2021-1",
        "image_url": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=900&q=80",
        "premium_only": False,
        "comparables": [
            {"title": "Lada Vesta 2020", "year": 2020, "mileage": 52000, "price": 970000, "url": "https://market.example/vesta-1"},
            {"title": "Lada Vesta 2021", "year": 2021, "mileage": 43000, "price": 1020000, "url": "https://market.example/vesta-2"},
            {"title": "Lada Vesta 2022", "year": 2022, "mileage": 25000, "price": 1130000, "url": "https://market.example/vesta-3"},
            {"title": "Lada Vesta 2021", "year": 2021, "mileage": 49000, "price": 995000, "url": "https://market.example/vesta-4"},
            {"title": "Lada Vesta 2019", "year": 2019, "mileage": 63000, "price": 910000, "url": "https://market.example/vesta-5"},
            {"title": "Lada Vesta 2021", "year": 2021, "mileage": 45000, "price": 980000, "url": "https://market.example/vesta-6"},
            {"title": "Lada Vesta 2021", "year": 2021, "mileage": 47000, "price": 990000, "url": "https://market.example/vesta-7"},
            {"title": "Lada Vesta 2020", "year": 2020, "mileage": 51000, "price": 965000, "url": "https://market.example/vesta-8"},
            {"title": "Lada Vesta 2021", "year": 2021, "mileage": 41000, "price": 1010000, "url": "https://market.example/vesta-9"},
            {"title": "Lada Vesta 2022", "year": 2022, "mileage": 22000, "price": 1150000, "url": "https://market.example/vesta-10"},
        ],
    },
]


def build_seed_cars() -> list[dict]:
    items = []
    for row in SEED_CARS:
        average_price = calculate_average_price(row["year"], row["mileage"], row["comparables"])
        deviation_percent = calculate_deviation_percent(row["price"], average_price)
        status = classify_deviation(deviation_percent)
        items.append(
            {
                **row,
                "average_price": average_price,
                "deviation_percent": deviation_percent,
                "status": status,
            }
        )
    return items
