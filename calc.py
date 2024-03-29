from typing import Union


def calc(sign: str, a, b: int) -> Union[int, float]:
    """
    Fast calculations, dict mode with lambda func.
    """
    if sign == '/' and (a == 0 or b == 0):
        raise ZeroDivisionError('Dont do it')
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    return operations.get(sign)(a, b)


def r_input():
    sign = input()
    a = int(input())
    b = int(input())
    return sign, a, b


if __name__ == '__main__':
    print(calc(*r_input()))
