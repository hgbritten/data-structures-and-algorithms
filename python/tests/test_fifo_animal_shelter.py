import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import (
    AnimalShelter,
    Cat,
    Dog,
)


def test_animal_shelter():
    assert AnimalShelter


def test_enqueue_cat():
    a = AnimalShelter()
    c = Cat()
    a.enqueue(c)
    actual = a.dequeue("cat")
    excepted = c
    assert actual == excepted


# @pytest.mark.skip("pending")
def test_enqueue_cat1():
    a = AnimalShelter()
    c = Cat()
    d = Dog()
    a.enqueue(c)
    a.enqueue(d)
    actual = a.dequeue("cat")
    excepted = c
    assert actual == excepted
