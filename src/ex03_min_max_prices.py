"""
EX03 (Tuplas)
Devolver el mínimo y el máximo de una lista.
"""

def min_max_prices(prices: list[float]) -> tuple[float, float]:
    """
    Devuelve una tupla (mínimo, máximo).

    - Si prices está vacía, lanza ValueError.
    """
    if not prices:
        raise ValueError("La lista 'prices' no puede estar vacía.")

    minimo = min(prices)
    maximo = max(prices)
    return (minimo, maximo)
