from Abstract_Limit_Structure import AbstractStack
from Abstract_Limit_Structure import AbstractQueue
from generator import Generator
from SSD import SSD
from Node import Node


class Stack(AbstractStack):
    __node = Node(None)
    __head = __node
    __cur_top = __head

    def push(self, value: SSD) -> bool:
        head = self.__head
        top = self.__head.n
        new_el = Node(value)
        head.n = new_el
        new_el.n = top
        self.__cur_top = head.n

        return True

    def pop(self) -> [SSD, None]:
        if self.__head.n is not None:
            head = self.__head
            top = head.n
            new_top = top.n
            head.n = new_top
            self.__cur_top = new_top
            return top.data
        else:
            return None

    def top(self) -> [SSD, None]:
        if self.__cur_top is not None:
            return self.__cur_top.data
        else:
            return None


class Queue(AbstractQueue):
    __body = []
    __size = 0

    def enqueue(self, value: SSD) -> bool:
        self.__body.append(value)
        self.__size += 1
        return True

    def dequeue(self) -> [SSD, None]:
        if self.__size != 0:
            value = self.__body[0]
            self.__body.remove(value)
            self.__size -= 1
            return value
        else:
            return None

    def top(self) -> [SSD, None]:
        if self.__size != 0:
            return self.__body[0]
        else:
            return None


s = Stack()
q = Queue()
g = Generator()

print(f"{'*' * 25}STACK{'*' * 25}")
s.push(g.generator())
s.push(g.generator())
s.push(g.generator())
s.push(g.generator())
s.push(g.generator())

print(f"top : {s.top()}")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(f"top : {s.top()}")

print(f"{'*' * 25}QUEUE{'*' * 25}")
q.enqueue(g.generator())
q.enqueue(g.generator())
q.enqueue(g.generator())
q.enqueue(g.generator())
q.enqueue(g.generator())

print(f"top : {q.top()}")

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(f"top : {q.top()}")
