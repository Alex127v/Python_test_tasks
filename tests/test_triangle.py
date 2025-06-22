from triangle import get_triangle_kind

def test_equilateral():
    assert get_triangle_kind(11, 11, 11) == 'Равносторонний'

def test_isosceles():
    assert get_triangle_kind(10, 10, 7) == 'Равнобедренный'

def test_regular():
    assert get_triangle_kind(7, 2, 15) == 'Простой'