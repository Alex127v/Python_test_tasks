"""
    Проверить, является ли строка с пробелами палиндромом (а роза упала на лапу азора).
    Упростим задачу, допуская, что cлова в предложении разделяются только одним пробелом.
"""


def is_palindrom(s: str) -> bool:
    straight = ''.join(s.split())
    return straight == straight[::-1]


if __name__ == '__main__':
    assert is_palindrom('а роза упала на лапу азора')
    assert is_palindrom('лёша на полке клопа нашёл')
    print('All string is palindrom')

