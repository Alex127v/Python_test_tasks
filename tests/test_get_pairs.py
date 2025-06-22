from get_pairs import get_pairs_number

def test_range_7():
    assert get_pairs_number([1, 2, 4, 3, 5, 2], 7) == [(2, 5), (3, 4)]