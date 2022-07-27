# 69505419

class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        try:
            self.items.append(int(value))
        except ValueError:
            raise ValueError(
                'input data is not a number or sign not in operation list'
                )

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            raise IndexError('list out of range')

    def answer(self):
        try:
            return self.items[-1]
        except IndexError:
            raise IndexError('list is empty')


operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }


def calculated(input_str, stack: Stack):
    for i in input_str:
        if i not in operations.keys():
            stack.push(i)
        else:
            a, b = stack.items[-2], stack.items[-1]
            stack.pop(), stack.pop()
            try:
                stack.push(operations[i](a, b))
            except ZeroDivisionError:
                raise ZeroDivisionError('Division by zero is prohibited')


if __name__ == '__main__':
    input_str = [i for i in input().strip().split()]
    stack = Stack()
    calculated(input_str, stack)
    print(stack.answer())
