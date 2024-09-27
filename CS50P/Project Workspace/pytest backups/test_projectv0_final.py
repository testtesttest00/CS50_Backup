import pytest
import project
from project import TicTacToe as T, SPS as S, Connect4 as C

def test_startgame():
    assert project.startgame(False, "A") == "A"
    assert project.startgame(False, "B") == "B"

def test_welcome():
    assert project.welcome("A") == "A"
    assert project.welcome("B") == "B"

def test_secret():
    assert project.secret() == False
    assert project.secret("A") == False
    assert project.secret("Cheat") == True
    assert project.secret("cheat") == True
    with pytest.raises(TypeError):
        project.secret(123)
