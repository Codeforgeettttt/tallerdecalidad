"""Módulo de citas médicas (código base del taller)."""

PORCENTAJES = {"contributivo": 0.10, "subsidiado": 0.0, "particular": 1.0}


def calcular_copago(valor_consulta: float, tipo_afiliado: str) -> float:
    """Calcula el copago que paga el paciente.

    - "contributivo": 10 %. "subsidiado": 0. "particular": 100 %.
    - Valor negativo o tipo desconocido lanzan ValueError.
    - El resultado se redondea a 2 decimales.
    """
    if valor_consulta < 0:
        raise ValueError("El valor de la consulta no puede ser negativo")
    if tipo_afiliado not in PORCENTAJES:
        raise ValueError(f"Tipo de afiliado inválido: {tipo_afiliado}")
    return round(valor_consulta * PORCENTAJES[tipo_afiliado], 2)
