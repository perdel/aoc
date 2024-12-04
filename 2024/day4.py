import numpy as np
import re


def pattern_count(arr: np.ndarray, pattern: str) -> int:
    count: int = 0
    for a in arr:
        line = "".join(a)
        count += line.count(pattern)
    return count


def diag_pattern_count(arr: np.ndarray, pattern: str) -> int:
    count: int = 0
    diags = np.arange(-1 * (len(arr) - len(pattern)), len(arr) - len(pattern) + 1)
    for d in diags:
        line = "".join(arr.diagonal(d))
        count += line.count(pattern)
    return count


def find_XMAS(fname: str) -> int:
    data = np.loadtxt(fname=fname, dtype=str)
    char_arr = np.asarray([list(d) for d in data])
    total = 0
    # horizontal
    total += pattern_count(char_arr, "XMAS")
    total += pattern_count(char_arr, "SAMX")
    # vertical
    total += pattern_count(char_arr.T, "XMAS")
    total += pattern_count(char_arr.T, "SAMX")
    # diagonal
    total += diag_pattern_count(char_arr, "XMAS")
    total += diag_pattern_count(char_arr, "SAMX")
    # diagonal transposed
    total += diag_pattern_count(np.flip(char_arr, 0), "XMAS")
    total += diag_pattern_count(np.flip(char_arr, 0), "SAMX")
    return total


if __name__ == "__main__":
    input_file = "2024/day4.txt"
    print(find_XMAS(fname=input_file))
