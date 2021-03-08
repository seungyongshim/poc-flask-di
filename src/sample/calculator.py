from .calculator_helper import add, minus


class Calculator:
    def __init__(self, left: int, right: int):
        self._left = left
        self._right = right

    def add(self):
        return add(self._left, self._right)

    def minus(self):
        return minus(self._left, self._right)
