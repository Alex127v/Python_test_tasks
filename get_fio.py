"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""


def get_person_short_name(fio: str) -> str:
    list_name = fio.split()
    short_name = ''
    for i, word in enumerate(list_name):
        if i == 0:
            short_name += (word + ' ')
        elif i < 2:
            short_name += (word[0] + '. ')
        else:
            short_name += (word[0] + '.')
    return short_name

if __name__ == '__main__':
    assert get_person_short_name('Лермонтов Михаил Юрьевич') == 'Лермонтов М. Ю.'
    assert get_person_short_name('Есенин Сергей Александрович') == 'Есенин С. А.'
    assert get_person_short_name('Маяковский Владимир Владимирович') == 'Маяковский В. В.'
    print('All passed')

