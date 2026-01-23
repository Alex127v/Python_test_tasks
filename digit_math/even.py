
"""
Напишите функцию, которая возвращает true, если число является четным.
Подсказка: используйте % для определения остатка от деления: 10 % 3 = 1
"""


def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == '__main__':
    assert is_even(2), 'Test number 2'
    assert is_even(88), 'Test number 88'
    assert is_even(1024), 'Test number 1024'
    print('All test passed')