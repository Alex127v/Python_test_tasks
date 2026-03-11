from digit_math.canade import sub_array

def test_sub_array():
    assert(sub_array([4, -1, -1, 6])) == 8
    assert(sub_array([-100, 5, 6])) == 11
    assert(sub_array([-1, -2, -3])) == -1
    print('All test pass well')