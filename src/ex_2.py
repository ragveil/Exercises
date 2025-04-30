def calculate_tax(
    price: float, tax_rate: float, *, discount: float = 0.0, r: int = 2
) -> float:
    params = (price, tax_rate, discount, r)
    if not all(isinstance(x, (float | int)) for x in params):
        raise TypeError("Неверный тип параметров")

    if price <= 0:
        raise ValueError("Неверная цена")

    if 100 <= tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    price += price * tax_rate / 100
    return round(price - price * discount / 100, r)
