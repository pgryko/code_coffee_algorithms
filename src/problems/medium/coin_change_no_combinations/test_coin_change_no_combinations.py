from src.problems.medium.coin_change_no_combinations.coin_change_no_combinations import (
    max_coin_change_no_combinations,
)


def test_max_coin_change_no_combinations_zero_amount():
    assert max_coin_change_no_combinations(0, [1, 2, 5]) == 1


def test_max_coin_change_no_combinations_no_coins():
    assert max_coin_change_no_combinations(5, []) == 0


def test_max_coin_change_no_combinations_single_coin_exact_match():
    assert max_coin_change_no_combinations(5, [5]) == 1


def test_max_coin_change_no_combinations_single_coin_no_match():
    assert max_coin_change_no_combinations(3, [5]) == 0


def test_max_coin_change_no_combinations_multiple_coins_no_solution():
    assert max_coin_change_no_combinations(3, [2, 4]) == 0


def test_max_coin_change_no_combinations_multiple_coins_with_solution():
    assert max_coin_change_no_combinations(5, [1, 2, 5]) == 4


def test_max_coin_change_no_combinations_large_amount():
    assert max_coin_change_no_combinations(100, [1, 2, 5]) == 541


def test_max_coin_change_no_combinations_coins_with_one_only():
    assert max_coin_change_no_combinations(10, [1]) == 1
