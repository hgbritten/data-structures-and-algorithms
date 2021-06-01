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


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class PseudoQueue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def enqueue(self, value=None):
        if self.right.top == None:
            self.left.push(value)

        if (self.left.top == None) and self.right.top:
            while self.right.top:
                self.left.push(self.right.pop())
            self.left.push(value)
        return self.left.top.value

    def dequeue(self):
        if (self.left.top == None) and (self.right.top == None):
            return "empty"
        if self.left.top:
            while self.left.top:
                self.right.push(self.left.pop())
        return self.right.pop()
