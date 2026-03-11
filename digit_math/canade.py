"""
Максимальная сумма поддиапозона
"""
nums_1 = [4, -1, -1, 6]
nums_2 = [-100, 5, 6]
nums_3 = [-1, -2, -3]

def sub_array(nums: list[int])->int:
    current_sum = nums[0]   # Сразу говорим что текущая суммма это первый элемент
    max_sum = nums[0]       # Сразу определяем 0 элемент как максимум, для сравнений

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i]) # Что лучше?Начать с текущего, или с суммы?
        max_sum = max(max_sum, current_sum) # Лучшая сумма из поддиапозонов
    return max_sum


if __name__ == '__main__':
    assert(sub_array(nums_1)) == 8
    assert(sub_array(nums_2)) == 11
    assert(sub_array(nums_3)) == -1
    print('All assert pass well')
