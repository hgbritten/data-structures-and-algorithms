import pytest
from code_challenges.queues_with_stacks.queues_with_stacks import Stack, PseudoQueue
from code_challenges.stacks_and_queues.invalid import InvalidOperationError


def test_stack_queue():
    assert Stack


def test_stack_has_top_queue():
    s = Stack()
    assert s.top is None


def test_push_onto_empty_queue():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    excepted = "apple"
    assert actual == excepted


def test_push_onto_full_queue():
    s = Stack()
    s.push("apple")
    s.push("cucumber")
    s.push("phone")
    actual = s.top.value
    excepted = "phone"
    assert actual == excepted


def test_pop_queue():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_peek_queue():
    s = Stack()
    s.push("apple")
    actual = s.peek()
    expected = "apple"
    assert actual == expected


def test_pseudo():
    assert PseudoQueue


def test_pseudo_has_left_queue():
    sleft = Stack()
    sright = Stack()
    q = PseudoQueue(sleft, sright)
    assert q.left.top is None


def test_pseudo_has_right_queue():
    sleft = Stack()
    sright = Stack()
    q = PseudoQueue(sleft, sright)
    assert q.right.top is None


def test_pseudo_enqueue():
    sleft = Stack()
    sright = Stack()
    q = PseudoQueue(sleft, sright)
    q.enqueue("apple")
    actual = q.left.top.value
    excepted = "apple"
    assert actual == excepted


def test_pseudo_enqueue_multi():
    sleft = Stack()
    sright = Stack()
    q = PseudoQueue(sleft, sright)
    q.enqueue("apple")
    q.enqueue("bananas")
    q.enqueue("cucumbers")
    actual = q.left.top.value
    excepted = "cucumbers"
    assert actual == excepted


def test_pseudo_dequeue():
    sleft = Stack()
    sright = Stack()
    q = PseudoQueue(sleft, sright)
    q.enqueue("apple")
    q.enqueue("bananas")
    q.enqueue("cucumbers")
    actual = q.dequeue()
    excepted = "apple"
    assert actual == excepted


def test_pseudo_dequeue_multi():
    sleft = Stack()
    sright = Stack()
    q = PseudoQueue(sleft, sright)
    q.enqueue("apple")
    q.enqueue("bananas")
    q.enqueue("cucumbers")
    q.dequeue()
    actual = q.dequeue()
    excepted = "bananas"
    assert actual == excepted
