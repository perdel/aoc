from day4 import find_xmas


def test_find_xmas():
    counts = find_xmas("2024/tests/day4-input.txt")
    assert counts == 18
