from day5 import middle_page_number


def test_middle_page_number():
    result = middle_page_number(fname="2024/tests/day5-input.txt")
    assert result == 143
