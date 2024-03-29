# Астрологи объявили день очередей ограниченного размера.
# Тимофею нужно написать класс MyQueueSized,
# который принимает параметр max_size,
# означающий максимально допустимое количество элементов в очереди.

# Помогите ему —– реализуйте программу,
# которая будет эмулировать работу такой очереди.
# Функции, которые надо поддержать, описаны в формате ввода.

# Формат ввода
# В первой строке записано одно число — количество команд,
# оно не превосходит 5000.
# Во второй строке задан максимально допустимый размер очереди,
# он не превосходит 5000.
# Далее идут команды по одной на строке. Команды могут быть следующих видов:

# push(x) — добавить число x в очередь;
# pop() — удалить число из очереди и вывести на печать;
# peek() — напечатать первое число в очереди;
# size() — вернуть размер очереди;
# При превышении допустимого размера очереди нужно вывести «error».
# При вызове операций pop() или peek() для пустой очереди нужно вывести «None».


class MyQueueSized:

    def __init__(self, max_length) -> None:
        self.queue = [None for _ in range(max_length)]
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.q_size = 0

    def __is_empty(self):
        return self.q_size == 0

    def push(self, value):
        if self.q_size < self.max_length:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_length
            self.q_size += 1
        else:
            print('error')

    def pop(self):
        if self.__is_empty():
            return None
        tmp_link = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_length
        self.q_size -= 1
        return tmp_link

    def size(self):
        return(self.q_size)

    def peek(self):
        return self.queue[self.head]


def length_command():
    try:
        return int(input())
    except TypeError:
        raise TypeError('input data is not a number')


def length_massive():
    try:
        return int(input())
    except TypeError:
        raise TypeError('input data is not a number')


if __name__ == '__main__':
    def q_main(length_command: int, length_massive: int):
        q = MyQueueSized(length_massive)
        command_list = {
            'pop': q.pop,
            'peek': q.peek,
            'size': q.size
        }
        for i in range(length_command):
            command = input().split()
            if command[0] == 'push':
                q.push(command[1])
            else:
                print(command_list[command[0]]())

    q_main(length_command(), length_massive())
