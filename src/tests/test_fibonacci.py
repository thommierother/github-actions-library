import pytest

from my_math.my_math import fibonacci


def test_that_fibonacci_raises_value_error_for_negative_numbers():
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci(-10)
    with pytest.raises(ValueError):
        fibonacci(-100)


def test_that_fibonacci_returns_0_for_0():
    assert fibonacci(0) == 0


def test_that_fibonacci_returns_1_for_1():
    assert fibonacci(1) == 1


def test_that_fibonacci_returns_correct_values():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(30) == 832040
