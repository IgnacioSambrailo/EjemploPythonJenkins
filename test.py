import pytest
from main import *

# Tets unitarios básicos para probar pipeline de Jenkins.

def test_suma():
    assert sumar(2,3) == 5

def test_resta():
    assert restar(5,6) == -1

def test_multiplicacion():
    assert multiplicar(2,10) == 20

def test_division():
    assert dividir(10,2) == 5

def test_elevacion():
    assert elevar(2,5) == 32

def test_raiz_cuadrada():
    assert raiz_cuadrada(25) == 5
