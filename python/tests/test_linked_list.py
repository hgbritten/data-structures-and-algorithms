from data_structures.linked_list.linked_list import LinkedList, Node


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


def test_append():
    lst = LinkedList()
    lst.insert("a")
    lst.insert("c")
    lst.insert("f")
    lst.append("b")
    actual = lst.__str__()
    expected = "{f} -> {c} -> {a} -> {b} -> None"
    assert actual == expected


def test_append_multi():
    lst = LinkedList()
    lst.insert("{a}")
    lst.insert("{c}")
    lst.insert("{f}")
    lst.append("{b}")
    lst.append("{d}")
    lst.append("{e}")
    actual = lst.__str__()
    expected = "{f} -> {c} -> {a} -> {b} -> {d} -> {e} -> None"
    assert actual == expected


def test_append():
    lst = LinkedList()
    lst.insert("a")
    lst.insert("c")
    lst.insert("f")
    lst.append("b")
    assert lst.includes("b") == True


def test_to_string():
    lst = LinkedList()
    lst.insert("{c}")
    lst.insert("{b}")
    lst.insert("{a}")
    actual = lst.__str__()
    expected = "{a} -> {b} -> {c} -> None"
    assert actual == expected


def test_insert_before_middle():
    lst = LinkedList()
    lst.insert("{c}")
    lst.insert("{b}")
    lst.insert("{a}")
    lst.insert_before("{b}", "{d}")
    actual = lst.__str__()
    expected = "{a} -> {d} -> {b} -> {c} -> None"
    assert actual == expected


def test_insert_before_first():
    lst = LinkedList()
    lst.insert("{c}")
    lst.insert("{b}")
    lst.insert("{a}")
    lst.insert_before("{a}", "{d}")
    actual = lst.__str__()
    expected = "{d} -> {a} -> {b} -> {c} -> None"
    assert actual == expected


def test_insert_after_middle():
    lst = LinkedList()
    lst.insert("{c}")
    lst.insert("{b}")
    lst.insert("{a}")
    lst.insert_after("{b}", "{d}")
    actual = lst.__str__()
    expected = "{a} -> {b} -> {d} -> {c} -> None"
    assert actual == expected


def test_insert_after_last():
    lst = LinkedList()
    lst.insert("{c}")
    lst.insert("{b}")
    lst.insert("{a}")
    lst.insert_after("{c}", "{d}")
    actual = lst.__str__()
    expected = "{a} -> {b} -> {c} -> {d} -> None"
    assert actual == expected


# def test_insert_before():
#     lst = LinkedList(values=["apple", "banana", "duck"])
#     lst.insert_before("apple", "cucumber")
#     actual = str(lst)
#     expected = str(LinkedList(values=["apple", "banana", "cucumber", "duck"]))
#     assert actual == expected, lst


# def test_str_before():
#     lst = LinkedList()
