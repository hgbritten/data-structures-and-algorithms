from code_challenges.tree.tree import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class K_tree:
    def __init__(self):
        self.root = None


def fizz_buzz_tree(tree=None):
    q = Queue()
    q.enqueue(tree.root)

    # if not tree:
    #     return []

    while not q.is_empty():
        front = q.dequeue()
        while front:
            if front.value % 3 == 0 and front.value % 5 == 0:
                front.value = "FizzBuzz"
                break
            elif front.value % 5 == 0:
                front.value = "Buzz"
                break
            elif front.value % 3 == 0:
                front.value = "Fizz"
                break
            else:
                front.value = str(front.value)
                break

        if front.left:
            q.enqueue(front.left)

        if front.right:
            q.enqueue(front.right)

    return tree
