from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def clone(self, converter=None):
        value = self.value
        if converter:
            value = converter(value)
        return Node(value)


class K_tree:
    def __init__(self, root=None):
        self.root = root

    # def breadth_first(tree):
    #     if tree.root is None:
    #         return
    #     q = []
    #     q.append(tree.root)
    #     while q:
    #         fizz_val = fizz_buzz_tree(q[0].value)
    #         print(fizz_val)

    #         node = q.pop(0)
    #         for child in node.children:
    #             q.append(child)

    #     return q

    def breadth_first(self):
        q = Queue()
        collection = []
        q.enqueue(self.root)

        while not q.is_empty():
            node = q.dequeue()
            collection.append(node.value)
            for child in node.children:
                q.enqueue(child)

        return collection

    def clone(self, converter=None):
        self.converter = converter

        clone_root = self.root.clone(converter)
        clone_tree = K_tree(clone_root)
        pairs = Queue()

        pairs.enqueue((self.root, clone_root))

        while not pairs.is_empty():
            source_node, clone_node = pairs.dequeue()
            for source_child in source_node.children:
                clone_child = source_child.clone(converter)
                pair = (source_child, clone_child)
                pairs.enqueue(pair)
                clone_node.children.append(clone_child)
        return clone_tree


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
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    one.children = [two, five]
    two.children = [three, four]
    five.children = [six, seven, eight]
    three.children = [nine, ten]
    four.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    eight.children = [fourteen, fifteen]

    kt = K_tree()
    kt = K_tree(one)
    clone = kt.clone(fizzify)
    print(clone.breadth_first())
