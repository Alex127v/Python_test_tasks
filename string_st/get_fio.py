"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""


def get_person_short_name(fio: str) -> str:
    last_name, first_name, middle_name = fio.split()
    return f'{last_name} {first_name[0].upper()}. {middle_name[0].upper()}.'


if __name__ == '__main__':
    assert get_person_short_name('Лермонтов Михаил Юрьевич') == 'Лермонтов М. Ю.'
    assert get_person_short_name('Есенин Сергей Александрович') == 'Есенин С. А.'
    assert get_person_short_name('Маяковский Владимир Владимирович') == 'Маяковский В. В.'
    print('All passed')

