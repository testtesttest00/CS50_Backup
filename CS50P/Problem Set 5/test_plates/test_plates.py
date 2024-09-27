from plates import is_valid

def test_tooshort():
    for i in ["a", "A", "1", "!", " ", ""]:
        assert is_valid(i) == 0

def test_specialchar():
    for i in ["!!!!!!", "TEST_", "A B C", "G(L)"]:
        assert is_valid(i) == 0

def test_startingchar():
    for i in ["123CAR", "1!LOL", "!!XXX", "1234", "12"]:
        assert is_valid(i) == 0

def test_seq():
    for i in ["AAA12A", "AAAA01", "AA000A"]:
        assert is_valid(i) == 0
