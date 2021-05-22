from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList


def test_has_head_none():
    lst = LinkedList()
    assert lst.head is None


def test_node_value():
    node = Node("a")
    assert node.value == "a"


def test_insert():
    lst = LinkedList()
    lst.insert("b")
    assert lst.head.value == "b"


def test_includes():
    lst = LinkedList()
    lst.insert("a")
    lst.insert("c")
    lst.insert("f")
    assert lst.includes("a") == True


def test_string():
    lst = LinkedList()


def test_node_next_is_none():
    node = Node("app")
    assert node.next is None
