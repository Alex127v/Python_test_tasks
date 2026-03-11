from digit_math.eratosthen import prime_num

def test_eratosthen():
    assert prime_num(10) == [2, 3, 5, 7]
    assert prime_num(6) == [2, 3, 5]
    print('All test pass')