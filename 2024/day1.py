import numpy as np


def total_distance(fname: str) -> int:
    left, right = np.loadtxt(fname, unpack=True, dtype=int)
    return sum([abs(x - y) for x, y in zip(np.sort(left), np.sort(right))])


def similarity_score(fname: str) -> int:
    left, right = np.loadtxt(fname, unpack=True, dtype=int)
    return int(np.sum([np.sum(right[right / x == 1.0]) for x in left]))


if __name__ == "__main__":
    input_file = "2024/day1-input.txt"
    print(total_distance(input_file))
    print(similarity_score(input_file))
