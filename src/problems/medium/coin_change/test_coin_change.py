import pytest
from coin_change import (
    coin_change,
)  # Assuming the coin_change function is in a file named coin_change.py


def test_standard_case():
    assert coin_change([1, 2, 5], 11) == 3, "Standard case failed"


def test_single_coin_no_solution():
    assert coin_change([2], 3) == -1, "Single coin no solution case failed"


def test_zero_amount():
    assert coin_change([1], 0) == 0, "Zero amount case failed"


def test_single_coin_exact_match():
    assert coin_change([1], 1) == 1, "Single coin exact match case failed"


def test_multiple_ways_to_form_amount():
    assert coin_change([1, 3, 4, 5], 7) == 2, "Multiple ways to form amount case failed"


def test_large_amount_with_large_denominations():
    assert (
        coin_change([1, 2, 5, 10], 27) == 4
    ), "Large amount with large denominations case failed"


def test_no_coins():
    assert coin_change([], 7) == -1, "No coins case failed"


def test_single_coin_multiple_exact_matches():
    assert coin_change([7], 14) == 2, "Single coin multiple exact matches case failed"


def test_optimal_solution_with_multiple_coins():
    assert (
        coin_change([2, 5, 10, 1], 6) == 2
    ), "Optimal solution with multiple coins case failed"


def test_large_input_size():
    assert coin_change([1, 2, 5], 100) == 20, "Large input size case failed"


if __name__ == "__main__":
    pytest.main()
