import pytest
from sistema_bancario import sacar

def test_saque_valido():
    assert sacar(70, 100) == 30
    
def test_valor_invalido():
    assert sacar(100, 10) == "impossivel sacar esse valor!"
