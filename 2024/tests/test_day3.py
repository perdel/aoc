from day3 import scan_mul, scan_mul_toggle


def test_scan_mul():
    result = scan_mul("2024/tests/day3-input1.txt")
    assert result == 161


def test_scan_mul_toggle():
    result = scan_mul_toggle("2024/tests/day3-input2.txt")
    assert result == 48
