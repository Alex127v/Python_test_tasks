from digit_math.product_all_num import product_all

def test_productn_all_num():
    assert product_all([2, 2, 3, 4]) == [24, 24, 16, 12]
    assert product_all([0, 3, 4, 2]) == [24, 0, 0, 0]
    print('All test pass')