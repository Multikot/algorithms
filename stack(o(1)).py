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
    her = int(input())
    for i in range(her):
        data = input().split()
        if data[0] == 'push':
            stack.push(data[1])
        elif data[0] == 'pop':
            stack.pop()
        else:
            print(stack.get_max())


if __name__ == '__main__':
    command_stack()
