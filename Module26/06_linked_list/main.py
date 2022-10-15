from typing import Any, Optional

class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None)-> None:
        self.value = value
        self.next = next

    def __str__(self)-> str:
        return 'Node [{value}]'.format(value=str(self.value))

class Linkedlist:
    def __init__(self):
        self.head: Optional[Node] = None
        self.lenght = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'Linkedlist []'


    def append(self, elem: Any):
        new_code = Node(elem)
        self.lenght += 1
        if self.head is None:
            self.head = new_code
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_code


    def remove(self, index)-> None:
        cur_node = self.head
        cur_index = 0
        if self.lenght == 0 or self.lenght <= index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.lenght -= 1
                return

        prev = 0
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
        prev.next = cur_node.next
        self.lenght -= 1

    def get(self, index):
        cur_node = self.head
        cur_index = 0
        if self.lenght == 0 or self.lenght <= index:
            raise IndexError

        prev = 0
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_index += 1
            cur_node = cur_node.next

        return cur_node


my_list = Linkedlist()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

