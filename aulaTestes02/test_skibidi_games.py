import pytest
from skibidi_games import Skibidi_Games

def test_cadastro():
    bib = Skibidi_Games()
    bib.cadastrar_jogos("Sigma vs Skibidi, the game")
    assert bib.quantidade_jogos() == 1
    
test_cadastro()