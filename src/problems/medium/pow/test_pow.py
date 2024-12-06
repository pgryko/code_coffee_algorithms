import pytest

from src.problems.medium.pow.pow import my_pow


def test_positive_exponents():
    assert my_pow(2, 2) == 4
    assert my_pow(2, 3) == 8
    assert my_pow(3, 4) == 81


def test_zero_cases():
    assert my_pow(0, 1) == 0
    assert my_pow(0, 5) == 0
    assert my_pow(2, 0) == 1
    assert my_pow(100, 0) == 1


def test_negative_exponents():
    assert my_pow(2, -2) == pytest.approx(0.25)
    assert my_pow(4, -1) == pytest.approx(0.25)
    assert my_pow(2, -3) == pytest.approx(0.125)


def test_float_base():
    assert my_pow(2.5, 2) == pytest.approx(6.25)
    assert my_pow(0.5, 2) == pytest.approx(0.25)
    assert my_pow(1.5, 3) == pytest.approx(3.375)


def test_large_exponents():
    assert my_pow(2, 10) == 1024
    assert my_pow(1.1, 20) == pytest.approx(6.72749994932561)


def test_edge_cases():
    assert my_pow(1, 1000000) == 1
    assert my_pow(-2, 2) == 4
    assert my_pow(-2, 3) == -8


def test_precision():
    # Test that results maintain reasonable precision
    result = my_pow(1.0000001, 1000)
    assert abs(result - 1.0001) < 1e-4
