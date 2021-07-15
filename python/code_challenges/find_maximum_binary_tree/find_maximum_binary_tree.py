class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    def find_maximum_value(self):
        # base case
        def max_walk(root, max_num):

            if not root:
                return

            # visit
            if root.value > max_num:
                max_num = root.value

            # go left
            max_walk(root.left, max_num)

            max_walk(root.right, max_num)

        max_num = self.root.value

        max_walk(self.root, max_num)

        return max_num

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
