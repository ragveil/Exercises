import pytest

from src.ex_2 import calculate_tax


@pytest.mark.parametrize(
    "price, tax_rate, expected",
    [(124.2, 3.3, 128.3),
     (733.2, 10, 806.52),
     (241, 16.2, 280.04)],
)
def test_calculate_tax_default(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


@pytest.mark.parametrize(
    "price, tax_rate, discount, expected",
    [(124.2, 3.3, 9.2, 116.5),
     (733.2, 10, 16.8, 671.02),
     (241, 16.2, 54.1, 128.54)],
)
def test_calculate_tax_discount(price, tax_rate, discount, expected):
    assert calculate_tax(price, tax_rate, discount=discount) == expected


@pytest.mark.parametrize(
    "price, tax_rate, discount, r, expected",
    [
        (124.2, 3.3, 9.2, 4, 116.4951),
        (733.2, 10, 16.8, 5, 671.02464),
        (241, 16.2, 54.1, 3, 128.539),
    ],
)
def test_calculate_tax_rounded(price, tax_rate, discount, r, expected):
    assert calculate_tax(price, tax_rate, discount=discount, r=r) == expected


@pytest.mark.parametrize(
    "price, tax_rate, discount, r",
    [("100", 10, 15, 2),
     (100, "10", 15, 2),
     (100, 10, "15", 2),
     (100, 10, 15, "2")],
)
def test_calculate_tax_type_error(price, tax_rate, discount, r):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, r=r)


def test_calculate_tax_keys():
    with pytest.raises(TypeError):
        calculate_tax(124.2, 3.3, 9, 4)
