from sample.calculator import Calculator


def test_add():
    left = 3
    right = 1
    sut = Calculator(left, right)
    assert sut.add() is left + right


def test_minus():
    left = 3
    right = 1
    sut = Calculator(left, right)
    assert sut.minus() is left - right
