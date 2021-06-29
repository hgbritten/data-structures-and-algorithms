from code_challenges.hashmap_tree_intersection.hashmap_tree_intersection import (
    tree_intersection,
)
from code_challenges.tree.tree import BinaryTree, Node
import pytest


# @pytest.mark.skip("pending")
def test_tree():
    assert tree_intersection


def test_tree1():
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(25)
    tree.root.right = Node(75)
    tree.root.left.left = Node(20)
    tree.root.right.right = Node(80)
    tree.root.left.right = Node(40)
    tree2 = BinaryTree()
    tree2.root = Node(50)
    tree2.root.left = Node(25)
    tree2.root.right = Node(75)
    tree2.root.left.left = Node(20)
    tree2.root.right.right = Node(80)
    tree2.root.left.right = Node(40)
    actual = tree_intersection(tree, tree2)
    expected = [50, 25, 20, 40, 75, 80]
    assert actual == expected


def test_tree2():
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(25)
    tree.root.right = Node(75)
    tree.root.left.left = Node(20)
    tree.root.right.right = Node(80)
    tree.root.left.right = Node(40)
    tree2 = BinaryTree()
    tree2.root = Node(50)
    tree2.root.left = Node(3)
    tree2.root.right = Node(4)
    tree2.root.left.left = Node(6)
    tree2.root.right.right = Node(7)
    tree2.root.left.right = Node(8)
    actual = tree_intersection(tree, tree2)
    expected = [50]
    assert actual == expected
