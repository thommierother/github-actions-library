import pytest

from my_math.my_math import factorial


def test_that_factorial_raises_value_error_for_negative_numbers():
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(-10)
    with pytest.raises(ValueError):
        factorial(-100)


def test_that_factorial_returns_1_for_0_and_1():
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_that_factorial_returns_correct_values():
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(20) == 2432902008176640000


def test_factorial_on_big_number(benchmark):
    result = benchmark(factorial, 20)
    assert result == 2432902008176640000
