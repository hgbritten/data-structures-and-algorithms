from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class K_tree:
    def __init__(self):
        self.root = None

    @staticmethod
    def breadth_first(tree):
        if tree.root is None:
            return
        q = []
        q.append(tree.root)
        while q:
            fizz_val = fizz_buzz_tree(q[0].value)
            print(fizz_val)

            node = q.pop(0)
            for child in node.children:
                q.append(child)

        return q


def fizz_buzz_tree(tree):
    q = Queue()
    q.enqueue(tree.root)
    # new_tree = K_tree()
    while not q.is_empty():
        front = q.dequeue()
        # new_val = fizzify(front.value)
        front.value = fizzify(front.value)
        # new_node = Node(new_val)
        # print(new_node.value)

        for child in front.children:
            q.enqueue(child)
    return tree


def fizzify(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 5 == 0:
        return "Buzz"
    elif value % 3 == 0:
        return "Fizz"
    else:
        return str(value)


def new_tree():
    pass


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        if self.storage:
            return self.storage.pop()
        else:
            return "queue empty"

    def peek(self):
        if self.storage:
            return self.storage[-1]
        else:
            return "queue empty"
        # return self.dq[-1]

    def is_empty(self):
        return len(self.storage) == 0


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(15)

    one.children = [two, five]
    two.children = [three, four]
    five.children = [six, seven, eight]
    kt = K_tree()
    kt.root = one
    fizz_buzz_tree(kt)
