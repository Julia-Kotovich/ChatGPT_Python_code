class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)


# Usage:
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.size())  # Output: 3
print(stack.peek())  # Output: 30

stack.pop()

print(stack.size())  # Output: 2
print(stack.peek())  # Output: 20

print(stack.is_empty())  # Output: False
