"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    product_totals: dict[str, float] = {}

    for product, units in cart:
        if units < 0:
            raise ValueError(f"Cantidad negativa no permitida: {product} ({units})")
        if product not in PRICES:
            raise ValueError(f"Producto desconocido: {product}")

        cost = PRICES[product] * units
        product_totals[product] = product_totals.get(product, 0) + cost

    product_totals = {p: round(c, 2) for p, c in product_totals.items()}

    total_general = round(sum(product_totals.values()), 2)

    return product_totals, total_general
