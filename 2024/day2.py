import numpy as np


def num_safe_reports(fname: str) -> int:
    with open(fname, mode="r") as fp:
        safe_counter: int = 0
        while line := fp.readline():
            parsed_line: np.ndarray = np.asarray(list(map(int, line.strip().split())))
            delta = []
            for idx, p in enumerate(parsed_line):
                if idx < len(parsed_line) - 1:
                    delta.append(p - parsed_line[idx + 1])
            delta = np.asarray(delta)
            if np.all(delta > 0) or np.all(delta < 0):
                if np.all(abs(delta) >= 1) and np.all(abs(delta) <= 3):
                    safe_counter += 1
    return safe_counter


def num_safe_reports_dampener(fname: str) -> int:
    with open(fname, mode="r") as fp:
        safe_counter: int = 0
        while line := fp.readline():
            parsed_line: np.ndarray = np.asarray(list(map(int, line.strip().split())))
            delta = []
            for idx, p in enumerate(parsed_line):
                if idx < len(parsed_line) - 1:
                    delta.append(p - parsed_line[idx + 1])
            delta = np.asarray(delta)
            if np.all(delta > 0) or np.all(delta < 0):
                if np.all(abs(delta) >= 1) and np.all(abs(delta) <= 3):
                    safe_counter += 1
                    continue
            for i in range(len(parsed_line)):
                delta_try = []
                mod_line = np.delete(parsed_line, i)
                for idx, m in enumerate(mod_line):
                    if idx < len(mod_line) - 1:
                        delta_try.append(m - mod_line[idx + 1])
                delta_try = np.asarray(delta_try)
                if np.all(delta_try > 0) or np.all(delta_try < 0):
                    if np.all(abs(delta_try) >= 1) and np.all(abs(delta_try) <= 3):
                        safe_counter += 1
                        break

    return safe_counter


if __name__ == "__main__":
    input_file = "2024/day2-input.txt"
    print(num_safe_reports(input_file))
    print(num_safe_reports_dampener(input_file))
