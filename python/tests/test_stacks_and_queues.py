import pytest
from code_challenges.stacks_and_queues.stacks_and_queues import Stack, Queue
from code_challenges.stacks_and_queues.invalid import InvalidOperationError


def test_stack():
    assert Stack


def test_stack_has_top():
    s = Stack()
    assert s.top is None


def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    excepted = "apple"
    assert actual == excepted


def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("cucumber")
    s.push("phone")
    actual = s.top.value
    excepted = "phone"
    assert actual == excepted


def test_pop():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_peek():
    s = Stack()
    s.push("apple")
    actual = s.peek()
    expected = "apple"
    assert actual == expected


def test_is_empty():
    s = Stack()
    actual = s.isEmpty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"


def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"


def test_queue():
    assert Queue


def test_queue_has_rear():
    s = Queue()
    assert s.rear is None


# @pytest.mark.skip("pending")
def test_enqueue_onto_empty_queue():
    s = Queue()
    s.enqueue("apple")
    actual = s.rear.value
    excepted = "apple"
    assert actual == excepted


# @pytest.mark.skip("pending")
def test_enqueue_onto_full_queue():
    s = Queue()
    s.enqueue("apple")
    s.enqueue("cucumber")
    s.enqueue("phone")
    actual = s.rear.value
    excepted = "phone"
    assert actual == excepted


# @pytest.mark.skip("pending")
def test_dequeue_queue():
    s = Queue()
    s.enqueue("apple")
    actual = s.dequeue()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_peek_queue():
    s = Queue()
    s.enqueue("apple")
    actual = s.peek()
    expected = "apple"
    assert actual == expected


def test_peek_queue_long():
    s = Queue()
    s.enqueue("apple")
    s.enqueue("cucumber")
    s.enqueue("phone")
    actual = s.peek()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_is_empty_queue():
    s = Queue()
    actual = s.isEmpty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_peek_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.peek()

    assert str(e.value) == "Method not allowed on empty collection"


def test_dequeue_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"
