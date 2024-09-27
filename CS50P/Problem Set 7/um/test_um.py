from um import count

def test_inword():
    assert count("yummy") == 0
    assert count("yum") == 0
    assert count("umbrella") == 0

def test_stringedge():
    assert count("um") == 1
    assert count("um hi um") == 2
    assert count("um hi um yum um ok") == 3

def test_casing():
    assert count("hi Um ok uM oops UM bye") == 3

def test_specialchar():
    assert count("my favourite word is 'um'.\num i like (um) it a lot um.um, yeah") == 5
