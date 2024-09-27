import pytest
from unittest.mock import Mock
from jar import Jar
import jar

testjar1 = Jar()
testjar2 = Jar(3)

def test_capacity():
    assert testjar1.capacity == 12
    assert testjar2.capacity == 3

def test_size():
    with pytest.raises(ValueError):
        testjar2.size = 4

def test_init():
    assert bool(Jar()) == 1
    assert bool(Jar(5)) == 1
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    assert str(testjar1) == ""#"None"
    testjar1.deposit(3)
    assert str(testjar1) == "🍪🍪🍪"
    Jar.withdraw(testjar1, 2) #alternate way to call method
    assert str(testjar1) == "🍪"

mock = Mock(Jar())
mock.size = 0
mock.capacity = 12

def test_deposit():
    Jar.deposit(mock, 1)
    assert mock.size == 1
    Jar.deposit(mock, 12)
    assert mock.size == 13

def test_withdraw():
    mock.size = 2
    Jar.withdraw(mock, 1)
    assert mock.size == 1
    Jar.withdraw(mock, 2)
    assert mock.size == -1
#seems like mock.size does not have jar.size property conditionals
