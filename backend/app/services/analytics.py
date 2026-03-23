from __future__ import annotations

from statistics import mean


def select_market_prices(reference_year: int, reference_mileage: int, comparables: list[dict]) -> list[float]:
    filtered = []
    min_mileage = int(reference_mileage * 0.7)
    max_mileage = int(reference_mileage * 1.3)

    for item in comparables:
        year_ok = abs(item["year"] - reference_year) <= 2
        mileage_ok = min_mileage <= item["mileage"] <= max_mileage
        if year_ok and mileage_ok:
            filtered.append(float(item["price"]))

    if len(filtered) < 3:
        filtered = [float(item["price"]) for item in comparables]

    if not filtered:
        return []

    filtered.sort()
    trim_count = max(1, int(len(filtered) * 0.1)) if len(filtered) >= 10 else 0
    if trim_count and len(filtered) > trim_count * 2:
        filtered = filtered[trim_count:-trim_count]

    return filtered


def calculate_average_price(reference_year: int, reference_mileage: int, comparables: list[dict]) -> float:
    prices = select_market_prices(reference_year, reference_mileage, comparables)
    if not prices:
        return 0.0
    return round(mean(prices), 2)


def calculate_deviation_percent(lot_price: float, average_price: float) -> float:
    if average_price <= 0:
        return 0.0
    return round((lot_price - average_price) / average_price * 100, 2)


def classify_deviation(deviation_percent: float) -> str:
    if deviation_percent > 20:
        return "overpriced_high"
    if 5 < deviation_percent <= 20:
        return "overpriced"
    if -5 <= deviation_percent <= 5:
        return "market"
    if -20 <= deviation_percent < -5:
        return "underpriced"
    return "underpriced_high"
