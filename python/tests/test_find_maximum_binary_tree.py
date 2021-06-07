import pytest
from code_challenges.find_maximum_binary_tree.find_maximum_binary_tree import (
    BinarySearchTree,
    BinaryTree,
    Node,
)


# @pytest.mark.skip("pending")
def test_binary_tree():
    assert BinaryTree()


def test_binary_search_tree_find():
    assert BinarySearchTree()


@pytest.mark.skip("pending")
def test_binary_search_find():
    b = BinarySearchTree()
    b.add(2)
    b.add(7)
    b.add(5)
    b.add(11)
    b.add(6)
    b.add(4)
    actual = b.find_maximum_value()
    expected = 11
    assert actual == expected


@pytest.mark.skip("pending")
def test_pre_order():
    b = BinarySearchTree()
    b.add(2)
    b.add(7)
    b.add(5)
    b.add(11)
    b.add(6)
    b.add(4)
    actual = b.pre_order()
    expected = [2, 4, 5, 6, 7, 11]
    assert actual == expected


def new_test():
    b = BinaryTree()
    b.root = Node(2)
    b.root.left = Node(7)
    b.root.right = Node(5)
    actual = b.find_maximum_value()
    expected = 7
    assert actual == expected
