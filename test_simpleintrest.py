from simpleintrest import Simple_interest


def test_positive():
    assert Simple_interest(5000, 10, 2) == 1000

def test_zero():
    assert Simple_interest(5000, 0, 2) == 0

def test_negative():
    assert Simple_interest(-5000, 10, 2) == -1000