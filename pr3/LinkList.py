from AbstractStructure import AbstractStructure
from generator import Generator
from SSD import SSD
from Node import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = None
    __tail: [None, Node] = None
    size: int = 0

    def add(self, value: SSD, index: [None, int] = None) -> bool:
        if index is not None and (index < 0 or index > self.size):
            return False
        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
            self.size += 1
        elif index is None:
            current = self.__tail
            node = Node(value)
            current.next = node
            self.__tail = node

            # current = self.__head
            # while current.next:
            #     current = current.next
            # current.next = Node(value)
            self.size += 1
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
            self.size += 1
        return True

    def insert(self, value: SSD, index: int) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
        return True

    def find(self, value: SSD) -> [int, None]:
        i = 0
        current = self.__head
        try:
            while current.data != value:
                current = current.next
                i += 1
            return i
        except AttributeError:
            return None

    def get(self, index: int) -> object:
        if self.size <= index or index < 0:
            return None
        else:
            i = 0
            current = self.__head
            while current.next and i < index:
                current = current.next
                i += 1
            return current.data

    def remove(self, value: SSD) -> bool:
        current = self.__head
        if current is None:
            return False
        while current:
            try:
                if current.next.data == value:
                    current.next = current.next.next
                    break
            except AttributeError:
                pass
            if current.data == value:
                self.__head = current.next
                break
            current = current.next
        self.size -= 1
        return True

    def get_all(self) -> list:
        output = []
        current = self.__head
        while current is not None:
            output.append(current.data)
            current = current.next
        return output


if __name__ == "__main__":
    r = Generator()
    ssd1 = r.generator()
    ssd2 = r.generator()
    ssd3 = r.generator()
    ssd4 = r.generator()
    ssd5 = r.generator()
    ssd6 = r.generator()
    s_list = LinkList()
    print(f"""all RAMs: {[ssd1, ssd2, ssd3, ssd4, ssd5, ssd6]}
{"-" * 225}
add ssd1: {s_list.add(ssd1)}
add ssd2: {s_list.add(ssd2)}
add ssd3: {s_list.add(ssd3)}
add ssd4: {s_list.add(ssd4)}
add ssd5: {s_list.add(ssd5, 1)}
find: {s_list.find(ssd2)}
{"-" * 225}
get_all:  {s_list.get_all()}
size: {s_list.size}
{"-" * 225}
remove ssd5: {s_list.remove(ssd5)}
find: {s_list.find(ssd5)}
get_all:  {s_list.get_all()}
size: {s_list.size}
{"-" * 225}
get ssd1: {s_list.get(0)}
get ssd4: {s_list.get(3)}
get ssd5: {s_list.get(4)}
{"-" * 225}
insert ssd6: {s_list.insert(ssd6, 1)}
get_all:  {s_list.get_all()}
size: {s_list.size}
{"-" * 225}""")
