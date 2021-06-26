import pytest
from code_challenges.hashtable.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_add():
    ht = Hashtable()
    actual = ht.add("apple", 42)
    expected = None
    assert actual == expected


def test_get_banana():
    ht = Hashtable()
    ht.add("banana", 9)
    actual = ht.get("banana")
    expected = 9
    assert actual == expected


def test_unknown_key():
    ht = Hashtable()
    ht.add("banana", 9)
    actual = ht.get("cucumber")
    expected = None
    assert actual == expected


def test_hash_apple():
    ht = Hashtable
    actual = ht.hash("apple")
    assert 0 <= actual <= 1024


def test_hash_banana():
    ht = Hashtable
    actual = ht.hash("banana")
    assert 0 <= actual <= 1024
