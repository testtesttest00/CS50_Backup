import seasons
import pytest

def test_invalidformat():
    assert bool(seasons.Date("2000-12-30")) == 1 #Valid Format - Creation of class obj

    test = seasons.Date("2000-12-30")
    assert bool(test.date) == 1 #Valid Format - Present class attribute

    with pytest.raises(ValueError):
        seasons.Date("2000-30-12")  #Invalid Format - Absent class obj

    with pytest.raises(SystemExit):
        seasons.Date("30-Dec-2000") #Invalid Format - Absent class obj

    with pytest.raises(SystemExit):
        seasons.Date("30 December 2000") #Invalid Format - Absent class obj

    with pytest.raises(SystemExit):
        seasons.Date("12/30/2000") #Invalid Format - Absent class obj

    with pytest.raises(SystemExit):
        seasons.Date("30/12/2000") #Invalid Format - Absent class obj
