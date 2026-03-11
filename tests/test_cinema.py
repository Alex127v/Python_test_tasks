from digit_math.cinema import place_max_distanse

def test_place_max_distanse():
    assert place_max_distanse([1, 0, 0, 0, 1, 0, 0, 0, 1, 1]) == (2, 2)
    assert place_max_distanse([0, 0, 0, 1, 1]) == (0, 3)
    assert place_max_distanse([1, 1, 0, 0, 0]) == (4, 3)
    assert place_max_distanse([0, 0, 0, 0]) is None
    print('All test passed well')
    