from digit_math.prime_number_2 import is_prime_2

def test_prime_2():
    assert(is_prime_2(1)) is False    
    assert(is_prime_2(2)) is True
    assert(is_prime_2(3)) is True
    assert(is_prime_2(5)) is True
    print('All test pass') 