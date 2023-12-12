# test_final.py

from final_functions import sieve_of_eratosthenes, min_max_sum_variable, check_number

def test_sieve_of_eratosthenes():
    expected_result = [2, 3, 5, 7, 11, 13, 17, 19]
    result = sieve_of_eratosthenes(20)
    assert result == expected_result, "test_sieve_of_eratosthenes FAILED"

def test_min_max_sum_variable():
    expected_results = [
        ((1, 2, 3), (1, 3, 6)),
        ((-5, 0, 5), (-5, 5, 0)),
        ((10, 20, 30, 40), (10, 40, 100))
    ]
    for args, expected in expected_results:
        result = min_max_sum_variable(*args)
        assert result == expected, f"test_min_max_sum_variable{args} FAILED"

def test_check_number():
    test_cases = [
        (5, "Positive"),
        (0, "Zero"),
        (-5, "Negative")
    ]
    for num, expected in test_cases:
        result = check_number(num)
        assert result == expected, f"test_check_number{num} FAILED"
