from data_structures.linked_list.linked_list import LinkedList, Node, zip_lists


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


# def test_k():
#     lst = LinkedList()
#     assert lst.k([1, 2, 3, 4], 2) == 2


def test_kth_from_end_zero():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.k(0)
    expected = "cucumbers"
    assert actual == expected


def test_kth_from_end_two():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.k(2)
    expected = "apples"
    assert actual == expected


# def test_zip_list_1():
#     list_1 = LinkedList()
#     list_2 = LinkedList()
#     list_1.append("apples")
#     list_1.append("bananas")
#     list_2.append("pears")
#     list_2.append("artichoke")
#     actual = zip_lists(list_1, list_2)
#     expected = "apples", "pears", "bananas", "artichoke"
#     assert actual == expected


def test_zip_list2():
    list_1 = LinkedList(values=["apples"])
    list_2 = LinkedList(values=["pears"])
    actual = str(zip_lists(list_1, list_2))
    expected = "apples -> pears -> None"
    assert actual == expected


def test_zip_list():
    list_1 = LinkedList(values=["apples", "bananas", "cucumbers"])
    list_2 = LinkedList(values=["pears", "artichoke", "carrots"])
    actual = str(zip_lists(list_1, list_2))
    expected = "apples -> pears -> bananas -> artichoke -> cucumbers -> carrots -> None"
    assert actual == expected


def test_zip_list_first_longer():
    list_1 = LinkedList(values=["apples", "bananas", "cucumbers", "beans"])
    list_2 = LinkedList(values=["pears", "artichoke", "carrots"])
    actual = str(zip_lists(list_1, list_2))
    expected = "apples -> pears -> bananas -> artichoke -> cucumbers -> carrots -> beans -> None"
    assert actual == expected


def test_zip_list_second_longer():
    list_1 = LinkedList(values=["apples"])
    list_2 = LinkedList(values=["pears", "beans"])
    actual = str(zip_lists(list_1, list_2))
    expected = "apples -> pears -> beans -> None"
    assert actual == expected


# def test_insert_before():
#     lst = LinkedList(values=["apple", "banana", "duck"])
#     lst.insert_before("apple", "cucumber")
#     actual = str(lst)
#     expected = str(LinkedList(values=["apple", "banana", "cucumber", "duck"]))
#     assert actual == expected, lst


# def test_str_before():
#     lst = LinkedList()
