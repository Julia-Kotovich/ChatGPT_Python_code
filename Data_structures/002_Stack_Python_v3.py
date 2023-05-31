class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)


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
