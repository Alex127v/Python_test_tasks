"""
Применить к массиву побитовое ИЛИ, и сказать какое число получилось в итоге четное или не четное
"""

nums_1 = [2, 4, 6, 8]
nums_2 = [2, 4, 6, 7]
nums_3 = [1, 7, 5, 9]

def is_even_bit(nums: list[int])->str:
    
    for num in nums:
        if num & 1:
            return 'Not even'
    return 'Even'

if __name__ == '__main__':
    assert(is_even_bit(nums_1))== 'Even'
    assert(is_even_bit(nums_2)) == 'Not even'
    assert(is_even_bit(nums_3)) == 'Not even'
    print('All assert pass')
