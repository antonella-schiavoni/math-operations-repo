"""
Test module for mathematical operations using pytest.
Tests all functions in the math_operations module.
"""

import pytest
from math_operations import add, subtract, multiply, divide


def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -3) == -8
    assert add(2.5, 3.5) == 6.0


def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(-1, -1) == 0
    assert subtract(-5, 3) == -8
    assert subtract(5.5, 2.5) == 3.0


def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(2.5, 4) == 10.0


def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-6, 2) == -3
    assert divide(-6, -2) == 3
    assert abs(divide(1, 3) - 0.3333333333333333) < 1e-15


def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)