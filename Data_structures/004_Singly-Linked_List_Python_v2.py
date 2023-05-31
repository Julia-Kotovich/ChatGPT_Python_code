class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError("Target data not found in the list")

    def delete(self, data):
        if self.is_empty():
            raise ValueError("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError("Data not found in the list")

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Usage:
sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.prepend(5)
sll.insert_after(20, 25)
sll.delete(10)

sll.display()  # Output: 5 -> 20 -> 25 -> 30 -> None
