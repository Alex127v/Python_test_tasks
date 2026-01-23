from string_st.get_fio import get_person_short_name

def test_lermontov():
    assert get_person_short_name('Лермонтов Михаил Юрьевич') == 'Лермонтов М. Ю.'
    assert get_person_short_name('Есенин Сергей Александрович') == 'Есенин С. А.'
    assert get_person_short_name('Маяковский Владимир Владимирович') == 'Маяковский В. В.'
    print('All test pass')
    


    

