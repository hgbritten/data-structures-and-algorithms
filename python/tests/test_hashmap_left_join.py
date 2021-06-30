import pytest
from code_challenges.hashtable.hashtable import Hashtable
from code_challenges.hashmap_left_join.hashmap_left_join import left_join


def test_hashmap():
    assert left_join


def test_left():
    ht1 = Hashtable()
    ht2 = Hashtable()
    ht1.add("fond", "enamored")
    ht1.add("wrath", "anger")
    ht1.add("diligent", "employed")
    ht2.add("fond", "averse")
    ht2.add("wrath", "delight")
    ht2.add("diligent", "follow")
    actual = left_join(ht1, ht2)
    expected = [
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "follow"],
        ["fond", "enamored", "averse"],
    ]
    for entry in expected:
        assert entry in actual


def test_left1():
    ht1 = Hashtable()
    ht2 = Hashtable()
    ht1.add("1", "enamored")
    ht1.add("2", "anger")
    ht1.add("3", "employed")
    ht2.add("1", "averse")
    ht2.add("2", "delight")
    ht2.add("3", "follow")
    actual = left_join(ht1, ht2)
    expected = [
        ["1", "enamored", "averse"],
        ["2", "anger", "delight"],
        ["3", "employed", "follow"],
    ]
    assert actual == expected


def test_left2():
    ht1 = Hashtable()
    ht2 = Hashtable()
    ht1.add("fond", "enamored")
    ht1.add("wrath", "anger")
    ht1.add("diligent", "employed")
    ht1.add("happy", "excited")
    ht2.add("fond", "averse")
    ht2.add("wrath", "delight")
    ht2.add("diligent", "follow")
    ht2.add("happy", "sad")

    actual = left_join(ht1, ht2)
    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "follow"],
        ["happy", "excited", "sad"],
    ]
    for entry in expected:
        assert entry in actual
