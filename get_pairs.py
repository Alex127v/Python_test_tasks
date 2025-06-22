"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""


def get_pairs_number(lst: list[int], n: int) -> list[tuple]:
    list_tuple = []
    unique_list = list(set(lst))
    unique_n = len(unique_list)
    i = 1
    for num_1 in range(unique_n - 1):
        for num_2 in range(i, unique_n):
            if unique_list[num_1] + unique_list[num_2] == n:
                list_tuple.append(tuple([unique_list[num_1], unique_list[num_2]]))
        i += 1
    return list_tuple
if __name__ == '__main__':
    assert get_pairs_number([1, 2, 4, 3, 5, 2], 7) == [(2, 5), (3, 4)]





