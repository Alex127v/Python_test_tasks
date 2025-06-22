from list_growing import is_list_growing

def test_range_1():
    assert is_list_growing([1.2, 2.4, 3.1, 8.2])

def test_range_2():
    assert is_list_growing([70.1, 70.3, 71.4, 71.5])
