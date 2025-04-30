def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


# print(calculate_taxes([200.0, 150.0, 123.0, 430.0], 10))
# print(calculate_taxes([200.0, 150.0, 123.0, 430.0], 5))
# print(calculate_taxes([100.0, 0.0, 200.5], 5))
# print(calculate_taxes([100.0, 0.5, 200.5], 5))
# print(calculate_taxes([100.0, 230.5, 200.5], 0))
