"""
Напишите функцию, которая возращает true, если число является простым
"""


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':

    assert is_prime(2), (2)
    assert is_prime(3), (3)
    assert is_prime(5), (5)
    assert is_prime(7), (7)
    assert is_prime(11), (11)
    assert is_prime(13), (13)
    print('All prime')

