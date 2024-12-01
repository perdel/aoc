from day1 import total_distance, similarity_score


def test_total_distance():
    distance_tot = total_distance("2024/tests/day1-input.txt")
    assert distance_tot == 11


def test_similarity_score():
    sim_score = similarity_score("2024/tests/day1-input.txt")
    assert sim_score == 31
