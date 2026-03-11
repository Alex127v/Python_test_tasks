from digit_math.first_last_ind import first_last_ind

def test_first_last_ind():
    lst_1 = [8, 2, 3, 2, 5, 6, 2]
    lst_2 = [9, 3, 4, 5, 7, 7]
    lst_3 = [7]
    lst_4 = []
    assert first_last_ind(lst_1, 2) == [0, 2]
    assert first_last_ind(lst_2, 7) == [3, 4]
    assert first_last_ind(lst_3, 7) == [0, 0]
    assert first_last_ind(lst_4, 5) == [-1, -1]
    print('All test pass')