class Node:
        def __init__(self, value = None, next = None):
            self.value = value
            self.next = next
        def __str__(self):
            return self.value

class ListQueue:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.var_size = 0

    def is_empty(self):
        return self.var_size == 0

    def put(self, value):
        if self.is_empty():
            self.head = Node(value=value)
            self.tail = self.head
        else:
            self.tail.next = Node(value=value)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.var_size += 1

    def get(self):
        if self.is_empty():
            return 'error'
        if self.var_size == 1:
            temp = self.head
            self.head = Node()
            self.tail = Node()
            self.var_size -= 1
            return temp
        if self.var_size == 2:
            temp = self.head
            self.head = self.tail
            self.var_size -= 1
            return temp
        temp = self.head
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.var_size -= 1
        return temp


    def size(self):
        return self.var_size


if __name__ == '__main__':
    list_q = ListQueue()
    command_list = {
        'get': list_q.get,
        'size': list_q.size
    }
    
    for _ in range(int(input())):
        command = input().split()
        if command[0] == 'put':
            list_q.put(command[1])
        else:
            print(command_list[command[0]]())
