import re


def scan_mul(fname: str) -> int:
    total = []
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    with open(fname, mode="r") as fp:
        while line := fp.readline():
            matches = pattern.finditer(line)
            for m in matches:
                a = int(m.group(1))
                b = int(m.group(2))
                total.append(a * b)
    return sum(total)


def scan_mul_toggle(fname: str) -> int:
    total = []
    control_pattern = re.compile(r"do\(\)|don't\(\)")
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    all_lines = []
    with open(file=fname, mode="r") as fp:
        while line := fp.readline():
            all_lines.append(line.strip())
    concat_lines = "".join(all_lines)
    selector = [True] * len(concat_lines)
    toggle = {"do()": [0], "don't()": []}
    control_matches = control_pattern.finditer(concat_lines)
    for c in control_matches:
        toggle[c.group()].append(c.span()[0])
    toggle["do()"].reverse()
    toggle["don't()"].reverse()
    do_idx = toggle["do()"].pop()
    dont_idx = toggle["don't()"].pop()
    for i in range(len(selector)):
        if i == do_idx:
            if len(toggle["do()"]) != 0:
                do_idx = toggle["do()"].pop()
            val = True
        if i == dont_idx:
            if len(toggle["don't()"]) != 0:
                dont_idx = toggle["don't()"].pop()
            val = False
        selector[i] = val
    matches = pattern.finditer(concat_lines)
    hits = []
    for m in matches:
        a = int(m.group(1))
        b = int(m.group(2))
        idx = m.start()
        hits.append([a * b, idx])
    total = []
    for h in hits:
        if selector[h[1]]:
            total.append(h[0])
    return sum(total)


if __name__ == "__main__":
    input_file = "2024/day3-input.txt"
    print(scan_mul(fname=input_file))
    print(scan_mul_toggle(fname=input_file))
