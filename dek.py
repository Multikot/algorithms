# 69504558

class Dek:
    ERROR = 'error'

    def __init__(self, max_length) -> None:
        self.__queue = [None for _ in range(max_length)]
        self._max_length = max_length
        self._head = 0
        self._tail = 0
        self._q_size = 0

    def __is_empty(self):
        return self._q_size == 0

    def __is_not_over_max(self):
        return self._q_size < self._max_length

    def push_front(self, value):
        if not self.__is_not_over_max():
            return print(self.ERROR)
        self.__queue[self._head - 1] = value
        self._head = (self._head - 1) % self._max_length
        self._q_size += 1

    def push_back(self, value):
        if not self.__is_not_over_max():
            return print(self.ERROR)
        self.__queue[self._tail] = value
        self._tail = (self._tail + 1) % self._max_length
        self._q_size += 1

    def pop_front(self):
        if self.__is_empty():
            return self.ERROR
        tmp_lnk = self.__queue[self._head]
        self.__queue[self._head] = None
        self._head = (self._head + 1) % self._max_length
        self._q_size -= 1
        return tmp_lnk

    def pop_back(self):
        if self.__is_empty():
            return self.ERROR
        tmp_lnk = self.__queue[self._tail - 1]
        self.__queue[self._tail - 1] = None
        self._tail = (self._tail - 1) % self._max_length
        self._q_size -= 1
        return tmp_lnk


def processing_operations(count_commands):
    for _ in range(count_commands):
        command = input().split()
        if command[0] in ('push_back', 'push_front'):
            command_list[command[0]](command[1])
        else:
            print(command_list[command[0]]())


if __name__ == '__main__':
    count_commands = int(input())
    dek = Dek(int(input()))
    command_list = {
        'push_back': dek.push_back,
        'push_front': dek.push_front,
        'pop_back': dek.pop_back,
        'pop_front': dek.pop_front
    }

    processing_operations(count_commands)
