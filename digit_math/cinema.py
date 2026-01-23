"""
Найти место в кинотеатре максимально удаленной от других. Вернуть его индекс и удаление.
При равных удалениях брать минимальный индекс
"""

seats_1 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
seats_2 = [0, 0, 0, 1, 1]
seats_3 = [1, 1, 0, 0, 0]
seats_4 = [0, 0, 0, 0]

def place_max_distanse(s: list[int])->tuple[int, int]|None:
    if  not any(s):
        return None
    occupeid = [i for i, n in enumerate(s) if n==1]
    candidate = []

    first = occupeid[0]
    if first > 0:
        candidate_ind = 0
        distance = first
        candidate.append((candidate_ind, distance))

    last = occupeid[-1]
    if last < (len(s) - 1):
        candidate_ind = len(s) - 1
        distance = candidate_ind - last
        candidate.append((candidate_ind, distance))

    for i in range(len(occupeid)-1):
        a = occupeid[i]
        b = occupeid[i+1]
        diff = b - a
        if diff > 1:
            distance = diff//2
            candidate_ind = a + distance
            candidate.append((candidate_ind, distance))
    vacant_best = max(candidate, key=lambda x: (x[1], -x[0]))
    return  vacant_best 
if __name__ == '__main__':
    assert place_max_distanse(seats_1) == (2, 2)
    assert place_max_distanse(seats_2) == (0, 3)
    assert place_max_distanse(seats_3) == (4, 3)
    assert place_max_distanse(seats_4) is None
    print('All assert passed well')




