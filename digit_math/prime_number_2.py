"""
Если число простое верни True, если нет False
"""

def is_prime_2(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':

    assert(is_prime_2(1)) is False    
    assert(is_prime_2(2)) is True
    assert(is_prime_2(3)) is True
    assert(is_prime_2(5)) is True
    print('All test pass')
    