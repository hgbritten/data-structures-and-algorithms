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

    def in_order(self):
        pass

    def post_order(self):
        pass


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
