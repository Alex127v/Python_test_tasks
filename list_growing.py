"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""

def is_list_growing(lst: list[float]) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True
if __name__ == '__main__':
    assert is_list_growing([1.2, 2.4, 3.1, 8.2])
    assert is_list_growing([70.1, 70.3, 71.4, 71.5])
    print('All list growing')