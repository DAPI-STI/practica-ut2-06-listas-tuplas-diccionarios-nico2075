"""
EX02 (Listas)
Eliminar duplicados manteniendo el orden de aparición.
"""

def unique_preserve_order(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista sin duplicados, manteniendo el orden.
    """
    seen = set()  
    result = []   
    
    for value in values:
        if value not in seen:
            result.append(value)
            seen.add(value)
            
    return result
