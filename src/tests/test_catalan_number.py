import pytest

from my_math.my_math import catalan_number


def test_that_catalan_number_raises_value_error_for_negative_numbers():
    with pytest.raises(ValueError):
        catalan_number(-1)
    with pytest.raises(ValueError):
        catalan_number(-10)
    with pytest.raises(ValueError):
        catalan_number(-100)


def test_that_catalan_number_returns_correct_values():
    assert catalan_number(0) == 1
    assert catalan_number(1) == 1
    assert catalan_number(2) == 2
    assert catalan_number(5) == 42
