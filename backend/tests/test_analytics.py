from app.services.analytics import (
    calculate_average_price,
    calculate_deviation_percent,
    classify_deviation,
    select_market_prices,
)


def test_select_market_prices_trims_outliers():
    comparables = [{"year": 2020, "mileage": 100000, "price": price} for price in [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]]
    prices = select_market_prices(2020, 100000, comparables)
    assert prices == [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


def test_average_and_status():
    comparables = [
        {"year": 2021, "mileage": 50000, "price": 1000000},
        {"year": 2021, "mileage": 55000, "price": 1050000},
        {"year": 2020, "mileage": 45000, "price": 950000},
    ]
    avg = calculate_average_price(2021, 50000, comparables)
    deviation = calculate_deviation_percent(850000, avg)
    assert avg == 1000000
    assert deviation == -15.0
    assert classify_deviation(deviation) == "underpriced"
