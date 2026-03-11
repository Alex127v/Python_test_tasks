"""
На вход не отсортированый список, выход - позиции первого и последнего 
заданного элемента  в отсортированном списке. Если цель не найдена вернуть [-1, -1]
"""
import bisect
lst_1 = [8, 2, 3, 2, 5, 6, 2]
lst_2 = [9, 3, 4, 5, 7, 7]
lst_3 = [7]
lst_4 = []
def first_last_ind(lst: list[int], target: int)->list[int]:
    
    if not lst: # Пустой список это False
        return [-1, -1]
    
    sort_lst = sorted(lst)   
    
    first_ind = bisect.bisect_left(sort_lst, target)    
    last_ind = bisect.bisect_right(sort_lst, target) # Тут нужо -1 т.к. получаем крайний индекс вставки
    if first_ind <= last_ind:     # Если цели нет - не выполнится, а пустой мы проверили ранее.
        return [first_ind, last_ind]  # Если цель однавернет одиаковый индекс
    else:
        return [-1, -1]
    
if __name__ == '__main__':
    assert first_last_ind(lst_1, 2) == [0, 2]
    assert first_last_ind(lst_2, 7) == [3, 4]
    assert first_last_ind(lst_3, 7) == [0, 0]
    assert first_last_ind(lst_4, 5) == [-1, -1]
    print('All test pass')



    


