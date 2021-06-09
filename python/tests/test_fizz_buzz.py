import pytest
from code_challenges.fizz_buzz_tree.fizz_buzz_tree import K_tree, fizz_buzz_tree, Node
from code_challenges.tree.tree import Queue


def test_k():
    assert K_tree


@pytest.mark.skip("pending")
def test_K():
    tree = K_tree()
    tree.root = Node(1)
    tree.root.children[0] = Node(2)
    tree.root.children[1] = Node(3)
    tree.root.children[2] = Node(4)
    tree.root.children[0].children[0] = Node(5)
    actual = fizz_buzz_tree(tree.breadth_first(tree))
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    assert actual == expected


def test_new():
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
    actual = fizz_buzz_tree(kt)
    actual1 = actual.root.children[1].children[2].value
    expected = "FizzBuzz"
    assert actual1 == expected


def test_new_1():
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
    actual = fizz_buzz_tree(kt)
    actual1 = actual.root.children[1].value
    expected = "Buzz"
    assert actual1 == expected


def test_new_2():
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
    actual = fizz_buzz_tree(kt)
    actual1 = actual.root.value
    expected = "1"
    assert actual1 == expected
