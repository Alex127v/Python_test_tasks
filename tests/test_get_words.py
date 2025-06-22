from get_words import get_words

def test_phrase_1():
    assert get_words('Александр Сергеевич Пушкин') == ['Александр', 'Сергеевич', 'Пушкин']

def test_phrase_2():
    assert get_words('Молоко машина возит') == ['Молоко', 'машина', 'возит']