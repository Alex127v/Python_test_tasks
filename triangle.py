"""
    Напишите функцию, которая принимает три положительных числа и
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""


def get_triangle_kind(a: int, b: int, c: int) -> str:
    if a == b and b == c:
        return 'Равносторонний'
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    return 'Простой'

if __name__ == '__main__':
    assert get_triangle_kind(11, 11, 11) == 'Равносторонний'
    assert get_triangle_kind(10, 10, 7) == 'Равнобедренный'
    assert get_triangle_kind(7, 2, 15) == 'Простой'
    print('All ok')