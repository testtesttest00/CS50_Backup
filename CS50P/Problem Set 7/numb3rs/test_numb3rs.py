#split on ".", outputs n1, n2, n3, n4
#check n[i] within list(range(276))
#nvm numb3rs does not make new ipv4 numbers lol
from numb3rs import validate

def test_numrange():
    assert validate("0.1.254.255") == 1
    assert validate("-1.5.567.999") == 0
    assert validate("1.999.999.999") == 0

def test_structure():
    assert validate("0..2.123") == 0
    assert validate("12.3.45") == 0

def test_char():
    assert validate("1,2,254,255") == 0
    assert validate("1 2 254 255") == 0
