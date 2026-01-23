"""
Является ли строка палиндромом? Вернуть True\False

"""

s = 'А   роза, упала! На? (лапу) - азора.'
s2 = 'Муза ранясь шилом опыта - ты помолишься ? На разуМ'

import re

def is_palindrom2(s: str)->bool:
    pattern = r'[а-яё0-9]+'    
    cleand = re.findall(pattern, s.lower())    
    return ''.join(cleand) == ''.join(cleand)[::-1]


if __name__ == '__main__':   
    assert is_palindrom2(s)
    assert is_palindrom2(s2)
    print('All is palindrom')
