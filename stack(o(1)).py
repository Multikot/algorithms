# Реализуйте класс StackMaxEffective,
# поддерживающий операцию определения максимума среди элементов в стеке.
# Сложность операции должна быть O(1).
# Для пустого стека операция должна возвращать None.
# При этом push(x) и pop() также должны выполняться за константное время.

# Формат ввода
# В первой строке записано одно число — количество команд,
# оно не превосходит 100000. Далее идут команды по одной в строке.
# Команды могут быть следующих видов:

# push(x) — добавить число x в стек;
# pop() — удалить число с вершины стека;
# get_max() — напечатать максимальное число в стеке;
# Если стек пуст, при вызове команды get_max нужно напечатать «None»,
# для команды pop — «error».
# Формат вывода
# Для каждой команды get_max() напечатайте результат её выполнения.
# Если стек пустой, для команды get_max() напечатайте «None».
# Если происходит удаление из пустого стека — напечатайте «error».


class Stack:
    def __init__(self):
        self.items = []
        self.tmp = -1 / 0.000000001
        self.max = []

    def _add(self, item):
        self.items.append(item)

    def push(self, item):
        if self.items == []:
            self._add(item)
            self.max.append(item)
        else:
            self._add(item)
            if int(item) >= int(self.max[-1]):
                self.max.append(item)

    def pop(self):
        try:
            if int(self.items[-1]) == int(self.max[-1]):
                self.max.pop()
            self.items.pop()
        except Exception:
            print('error')

    def get_max(self):
        try:
            return self.max[-1]
        except Exception:
            return None


stack = Stack()


def command_stack():
    data_input = int(input())
    for i in range(data_input):
        data = input().split()
        if data[0] == 'push':
            stack.push(data[1])
        elif data[0] == 'pop':
            stack.pop()
        else:
            print(stack.get_max())


if __name__ == '__main__':
    command_stack()
