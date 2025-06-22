from get_fio import get_person_short_name

def test_lermontov():
    assert get_person_short_name('Лермонтов Михаил Юрьевич') == 'Лермонтов М. Ю.'

def test_esenin():
    assert get_person_short_name('Есенин Сергей Александрович') == 'Есенин С. А.'

def test_mayakovsky():
    assert get_person_short_name('Маяковский Владимир Владимирович') == 'Маяковский В. В.'

