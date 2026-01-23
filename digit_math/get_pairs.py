"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""


def get_pairs_number(lst: list[int], N: int) -> list[tuple[int, int]]:
    set_pairs = set()
    for n in lst:
        for i in lst:
            if n + i == N:
                set_pairs.add((n, i) if n < i else (i, n))
    return list(set_pairs)


if __name__ == '__main__':
    assert get_pairs_number([1, 2, 4, 3, 5, 2], 7) == [(2, 5), (3, 4)]
    print('All pairs found')





