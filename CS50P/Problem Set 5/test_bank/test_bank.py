from bank import value

def test_hello():
    for i in ["hello", "Hello", "hellooo there"]:
        assert value(i) == 0

def test_h():
    for i in ["how bout you", "How Is It Going", "harambe1234"]:
        assert value(i) == 20

def test_noH():
    for i in ["my guy", "yo", "123", "!! !!"]:
        assert value(i) == 100
