from day2 import num_safe_reports, num_safe_reports_dampener


def test_num_safe_reports():
    n = num_safe_reports(fname="2024/tests/day2-input.txt")
    assert n == 2


def test_num_safe_reports_dampener():
    n = num_safe_reports_dampener(fname="2024/tests/day2-input.txt")
    assert n == 4
