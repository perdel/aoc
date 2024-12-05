def middle_page_number(fname: str) -> int:
    rules: list = []
    orderings: list = []
    with open(fname) as fp:
        while line := fp.readline():
            if "|" in line:
                rules.append(line.strip())
            elif "," in line:
                orderings.append(line.strip())

    split_orderings: list = [o.split(",") for o in orderings]

    take: list = []
    for s in split_orderings:
        good = True
        for idx in range(len(s) - 1):
            if "|".join((s[idx], s[idx + 1])) not in rules:
                good = False
                break
        if good:
            take.append(s)

    return sum([int(t[len(t) // 2]) for t in take])


if __name__ == "__main__":
    input_file: str = "2024/day5.txt"
    print(middle_page_number(fname=input_file))
