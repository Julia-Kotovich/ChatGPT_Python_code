class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)


# Usage:
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.size())  # Output: 3
print(queue.peek())  # Output: 10

queue.dequeue()

print(queue.size())  # Output: 2
print(queue.peek())  # Output: 20

print(queue.is_empty())  # Output: False
