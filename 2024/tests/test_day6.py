from day6 import visited_positions


def test_visited_positions():
    result = visited_positions("2024/tests/day6-input.txt")
    assert result == 41
