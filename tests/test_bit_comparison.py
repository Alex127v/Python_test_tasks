from digit_math.bit_comparison import is_even_bit

def test_is_even_bit():
    assert(is_even_bit([2, 4, 6, 8]))== 'Even'
    assert(is_even_bit([2, 4, 6, 7])) == 'Not even'
    assert(is_even_bit([1, 7, 5, 9])) == 'Not even'
    print('All tests pass')