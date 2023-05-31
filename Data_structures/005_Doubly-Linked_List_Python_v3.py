class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next
        raise ValueError("Target data not found in the list")

    def delete(self, data):
        if self.is_empty():
            raise ValueError("List is empty")
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
        raise ValueError("Data not found in the list")

    def display_forward(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

    def display_backward(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.tail
            while current:
                print(current.data, end=" <-> ")
                current = current.prev
            print("None")


# Usage:
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)
dll.insert_after(20, 25)
dll.delete(10)

dll.display_forward()  # Output: 5 <-> 20 <-> 25 <-> 30 <-> None
dll.display_backward()  # Output: 30 <-> 25 <-> 20 <-> 5 <-> None
