from code_challenges.stacks_and_queues.invalid import InvalidOperationError


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            val = self.top.value
            self.top = self.top.next
            return val
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def isEmpty(self):
        return self.top is None


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        if self.rear:
            self.rear = Node(value)
        else:
            self.rear = Node(value)
            self.front = self.rear

    def dequeue(self):
        if self.front:

            temp = self.front
            self.front = self.front.next
            temp.next = None

            return temp.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def isEmpty(self):
        return self.front is None
