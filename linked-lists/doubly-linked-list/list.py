from node import Node


class List:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def is_empty(self) -> bool:
        return self.head is None

    def print_all(self):
        tmp: Node = self.head
        while tmp is not None:
            print(tmp.key, end=", ")
            tmp = tmp.next
        print("")

    def number_of_elements(self) -> int:
        count: int = 0
        tmp: Node = self.head
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def add_to_head(self, key: int):
        if self.is_empty():
            self.head = self.tail = Node(key)
        else:
            self.head = Node(key, None, self.head)
            self.head.next.prev = self.head

    def add_to_tail(self, key: int):
        if self.is_empty():
            self.head = self.tail = Node(key)
        else:
            self.tail.next = Node(key, self.tail)
            self.tail = self.tail.next

    def delete_from_head(self) -> int:
        if self.is_empty():
            return None
        else:
            ret_node: Node = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return ret_node.key

    def delete_from_tail(self) -> int:
        if self.is_empty():
            return None
        else:
            ret_node: Node = self.tail
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev;
                self.tail.next = None
            return ret_node.key

    def delete_nodes_with_value(self, key: int):
        if self.is_empty():
            return None
        ret_value: int = None
        tmp: Node = self.head
        while tmp.next is not None:
            if tmp.next.key == key:
                ret_value = tmp.next.key
                tmp.next = tmp.next.next
                if tmp.next is not None:
                    tmp.next.prev = tmp
            else:
                tmp = tmp.next
        self.tail = tmp
        if self.head.key == key:
            ret_value = self.delete_from_head()
        return ret_value

    def delete_on_index(self, index: int):
        if self.is_empty():
            return
        end_index: int = self.number_of_elements() - 1
        if index < 0 or index > end_index:
            return
        if index == 0:
            self.delete_from_head()
        elif index == end_index:
            self.delete_from_tail()
        else:
            tmp: Node = self.head
            count: int = 0
            while count < index:
                tmp = tmp.next
                count += 1
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev

    def insert_after(self, list_element: int, new_element: int):
        tmp: Node = self.head
        while tmp is not None:
            if tmp.key == list_element:
                if tmp == self.tail:
                    self.add_to_tail(new_element)
                else:
                    new_node: Node = Node(new_element, tmp, tmp.next)
                    tmp.next = new_node
                    new_node.next.prev = new_node
                tmp = tmp.next
            tmp = tmp.next

    def insert_before(self, list_element: int, new_element: int):
        tmp: Node = self.head
        while tmp is not None:
            if tmp.key == list_element:
                if tmp == self.head:
                    self.add_to_head(new_element)
                else:
                    new_node: Node = Node(new_element, tmp.prev, tmp)
                    new_node.prev.next = new_node
                    tmp.prev = new_node
            tmp = tmp.next

    def sort(self):
        swapped: bool = True
        outer: Node = self.head
        inner: Node = self.tail
        while outer != self.tail:
            inner = self.tail
            while inner != outer:
                if inner.key < inner.prev.key:
                    k = inner.key
                    inner.key = inner.prev.key
                    inner.prev.key = k
                inner = inner.prev
            outer = outer.next


