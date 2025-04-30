import pytest

from src.ex_1 import calculate_taxes


@pytest.fixture
def prices():
    return [200.0, 150.0, 123.0, 430.0]


@pytest.mark.parametrize(
    "tax, expected",
    [
        (10.0, [220.0, 165.0, 135.3, 473.0]),
        (5.0, [210.0, 157.5, 129.15, 451.5]),
        (0.0, [200.0, 150.0, 123.0, 430.0]),
    ],
)
def test_taxed_prices(prices, tax, expected):
    assert calculate_taxes(prices, tax) == expected


@pytest.mark.parametrize(
    "price, tax", [([200.0, 150.0, 123.0, 430.0], -1.2),
                   ([10.5, 0, -4.2], 1.2)]
)
def test_taxed_prices_negative(price, tax):
    with pytest.raises(ValueError) as error_info:
        calculate_taxes(price, tax)
        assert str(error_info.value) == "Неверный налоговый процент"
    with pytest.raises(ValueError) as error_info:
        calculate_taxes(price, tax)
        assert str(error_info.value) == "Неверная цена"
