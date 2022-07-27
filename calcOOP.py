class Сalculated:

    __operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '%': lambda a, b: a % b,
        '//': lambda a, b: a // b
    }

    def __init__(self, value_1: str, value_2: str) -> None:
        self.value_1 = value_1
        self.value_2 = value_2

    def __error_or_float(self):
        try:
            return float(self.value_1), float(self.value_2)
        except Exception:
            raise TypeError('input data is not a number')

    def plus(self):
        return self.__operations.get('+')(*self.__error_or_float())

    def mines(self):
        return self.__operations.get('-')(*self.__error_or_float())

    def mult(self):
        return self.__operations.get('*')(*self.__error_or_float())

    def div(self):
        try:
            return self.__operations.get('/')(*self.__error_or_float())
        except ZeroDivisionError:
            raise ZeroDivisionError("Don't do it")

    def div_remains(self):
        return self.__operations.get('%')(*self.__error_or_float())

    def div_wit_rem(self):
        return self.__operations.get('//')(*self.__error_or_float())

    def all_operations(self):
        return (
            f'plus: {self.plus()}, mines: {self.mines()}',
            f'multiplication: {self.mult()}, division: {self.div()}',
            f'remains of division: {self.div_remains()}',
            f'division witwout remeins: {self.div_wit_rem()}'
            )


if __name__ == '__main__':

    def r_input():
        return (input() for i in range(2))
    q = Сalculated(*r_input())

    print(q.plus())
    print(q.mines())
    print(q.mult())
    print(q.div())
    print(q.div_remains())
    print(q.div_wit_rem())
    print(*q.all_operations())
