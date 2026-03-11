"""
Найти все числа простые, которые <=N
"""

N_1 = 10  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N_2 = 6 # [1, 2, 3, 4, 5, 6]

def prime_num(n: int)->list[int]:
    is_prime = [True]*(n+1)           # Делаем список для всех чисел до N, и говорим что они простые
    is_prime[0] = is_prime[1] = False  # Первые два элемента 0 и 1 - сразу не простые.

    for i in range(2, int(n**0.5)+1):  # Идем по индексам от 2 до корня из n, и если флаг True,
        if is_prime[i]:                # тогда начинаем переопределять все кратные числа с шагом i
            for j in range(i*i, n+1, i):  # Начинаем от i*i потому что это наименьший кратный, все что меньше, кратные, уже вычеркнуты
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]



if __name__ == '__main__':
    assert(prime_num(N_1)) == [2, 3, 5, 7]
    assert(prime_num(N_2)) == [2, 3, 5]
    print('All assert pass')