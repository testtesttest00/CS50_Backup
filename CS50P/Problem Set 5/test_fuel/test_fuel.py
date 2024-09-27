from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("100/10")
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    assert convert("10/100") == 10

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
