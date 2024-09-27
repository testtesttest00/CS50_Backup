from working import convert
import pytest

def test_with00():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:00 AM to 2:00 AM") == "11:00 to 02:00"

def test_without00():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 6 AM") == "22:00 to 06:00"

def test_hr12():
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12 AM to 7 PM") == "00:00 to 19:00"

def test_errrors():
    with pytest.raises(ValueError):
        convert("idk")
    with pytest.raises(ValueError):
        convert("7:60 AM to 5:00 PM")
