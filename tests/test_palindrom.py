from palindrom import is_palindrom

def test_first_phrase():
    assert is_palindrom('а роза упала на лапу азора')

def test_second_phrase():
    assert is_palindrom('лёша на полке клопа нашёл')
    