import numpy as np


def visited_positions(fname: str) -> int:
    raw_guide_map = np.loadtxt(fname=fname, dtype=str, comments=None)
    guide_map = np.asarray([list(r.strip()) for r in raw_guide_map])

    direction = "^"
    xpos, ypos = np.argwhere(guide_map == direction)[0]

    while (
        xpos != 0
        and xpos != guide_map.shape[0] - 1
        and ypos != 0
        and ypos != guide_map.shape[0] - 1
    ):
        old_pos = (xpos, ypos)
        if direction == "^":
            if guide_map[xpos - 1, ypos] != "#":
                xpos -= 1
            else:
                direction = ">"

        elif direction == "v":
            if guide_map[xpos + 1, ypos] != "#":
                xpos += 1
            else:
                direction = "<"

        elif direction == "<":
            if guide_map[xpos, ypos - 1] != "#":
                ypos -= 1
            else:
                direction = "^"

        elif direction == ">":
            if guide_map[xpos, ypos + 1] != "#":
                ypos += 1
            else:
                direction = "v"

        guide_map[old_pos] = "X"
    return len(np.argwhere(guide_map == "X")) + 1


if __name__ == "__main__":
    input_file: str = "2024/day6.txt"
    print(visited_positions(fname=input_file))
