'''Самая лучшая программа для вычисления квадратного корня из
заданного числа'''

from math import sqrt


def calculate_squareroot(number: float) -> float:
    '''Вычисляет квадратный корень.'''
    return sqrt(number)


def calc(your_number: float) -> None:
    '''Производит арифметические операции.'''
    if your_number <= 0:
        return

    result: float = calculate_squareroot(your_number)

    print(
        'Мы вычислили квадратный корень из '
        f'введённого вами числа ({your_number}). Это будет: {result}'
    )


if __name__ == '__main__':
    message = (
        'Добро пожаловать в самую лучшую программу для вычисления '
        'квадратного корня из заданного числа'
    )

    print(message)
    calc(25.5)
