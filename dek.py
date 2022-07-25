#69491240

class Dek:
    ERROR = 'error'

    def __init__(self, max_length) -> None:
        self.queue = [None for _ in range(max_length)]
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.q_size = 0

    def __is_empty(self):
        return self.q_size == 0
    
    def __is_not_over_max(self):
        return self.q_size < self.max_length

    def push_front(self, value):
        if self.__is_not_over_max():
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_length
            self.q_size += 1
        else:
            print(self.ERROR)

    def push_back(self, value):
        if self.__is_not_over_max():
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_length
            self.q_size += 1
        else:
            print(self.ERROR)

    def pop_front(self):
        if self.__is_empty():
            return self.ERROR
        tmp_lnk = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_length
        self.q_size -= 1
        return tmp_lnk

    def pop_back(self):
        if self.__is_empty():
            return self.ERROR
        tmp_lnk = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_length
        self.q_size -= 1
        return tmp_lnk

    
if __name__ == '__main__':
    count_commands = int(input())
    dek = Dek(int(input()))
    command_list = {
        'push_back': dek.push_back,
        'push_front': dek.push_front,
        'pop_back': dek.pop_back,
        'pop_front': dek.pop_front
    }
    for _ in range(count_commands):
        command = input().split()
        if command[0] in ('push_back', 'push_front'):
            command_list[command[0]](command[1])
        else:
            print(command_list[command[0]]())