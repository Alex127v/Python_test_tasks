from string_st.palindrom2 import is_palindrom2

def test_palindrom2():
    s = 'А   роза, упала! На? (лапу) - азора.'
    s2 = 'Муза ранясь шилом опыта - ты помолишься ? На разуМ'
    assert is_palindrom2(s)
    assert is_palindrom2(s2)
    print('All test pass')




