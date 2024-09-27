import twttr

def test_vowel():
    assert twttr.shorten("aeiou") == ""
    assert twttr.shorten("AaA") == ""

def test_consonant():
    assert twttr.shorten("Hjk") == "Hjk"
    assert twttr.shorten("qwxy") == "qwxy"

def test_symbol():
    assert twttr.shorten("!@*,-123") == "!@*,-123"

def test_mix():
    assert twttr.shorten("Hi!") == "H!"
    assert twttr.shorten("Username: J@5on_") == "srnm: J@5n_"
