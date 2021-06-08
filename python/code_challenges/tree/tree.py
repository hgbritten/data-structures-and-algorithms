from code_challenges.stacks_and_queues.invalid import InvalidOperationError
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.dq = deque()

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
        # return self.dq[-1]

    def isEmpty(self):
        return self.front is None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        visit root then left then right
        """

        def walk(root, collection):
            # base case
            if not root:
                return

            # visit
            collection.append(root.value)

            # go left
            walk(root.left, collection)

            walk(root.right, collection)

        collected_values = []

        walk(self.root, collected_values)

        return collected_values

    def in_order(self):
        def walk(root, collection):
            if not root:
                return

            walk(root.left, collection)

            collection.append(root.value)

            walk(root.right, collection)

        collected_values = []

        walk(self.root, collected_values)

        return collected_values

    def post_order(self):
        def walk(root, collection):
            if not root:
                return

            walk(root.left, collection)

            walk(root.right, collection)

            collection.append(root.value)

        collected_values = []

        walk(self.root, collected_values)

        return collected_values

    @staticmethod
    def breadth_first(tree):

        """
        // INPUT <-- root node
        // OUTPUT <-- front node of queue to console
        """
        values = []

        queue_breadth = Queue()
        queue_breadth.enqueue(tree.root)

        while queue_breadth.peek():
            front = queue_breadth.dequeue()
            values.append(front)

            if front.left:
                queue_breadth.enqueue(front.left)

            if front.right:
                queue_breadth.enqueue(front.right)

        return values


# ALGORITHM breadthFirst(root)
# // INPUT <-- root node
# // OUTPUT <-- front node of queue to console

#   Queue breadth <-- new Queue()
#   breadth.enqueue(root)

#   while breadth.peek()
#     node front = breadth.dequeue()
#     OUTPUT <-- front.value

#     if front.left is not NULL
#       breadth.enqueue(front.left)

#     if front.right is not NULL
#       breadth.enqueue(front.right)


class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = Node(value)

        def walk(root, node_to_add):
            if not root:
                return

            value_to_add = node_to_add.value

            if value_to_add < root.value:
                # get left
                if root.left:
                    walk(root.left, node_to_add)
                else:
                    root.left = node_to_add
            else:
                if root.right:
                    walk(root.right, node_to_add)
                else:
                    root.right = node_to_add
                # go right

        if not self.root:
            self.root = node
            return

        walk(self.root, node)

    def contains(self, value):
        def walk(root, value):
            if not root:
                return False
            return (
                root.value == value or walk(root.left, value) or walk(root.right, value)
            )

        return walk(self.root, value)
