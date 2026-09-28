import pytest

from src.citas import calcular_copago


def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


def test_contributivo_paga_10_por_ciento():
    assert calcular_copago(100000, "contributivo") == 10000


def test_subsidiado_no_paga():
    assert calcular_copago(100000, "subsidiado") == 0


def test_valor_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_copago(-1, "particular")


def test_tipo_invalido_lanza_error():
    with pytest.raises(ValueError):
        calcular_copago(100000, "vip")
