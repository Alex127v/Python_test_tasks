"""
Напишите функцию, которая возвращает true, если
три заданных числа (в указанном порядке) являются последовательными членами
арифметической прогрессии
"""


def is_arifm_progression(a: int, b: int, c: int) -> bool:
    return  b - a == c - b


if __name__ == '__main__':
    assert is_arifm_progression(3, 8, 13)
    assert is_arifm_progression(2, 6, 10)
    print('It is arifm_progression')