import pytest
from code_challenges.merge_sort.merge_sort import merge, merge_sort


# @pytest.mark.skip("pending")
def test_merge():
    assert merge_sort


def test_edge():
    actual = merge_sort([1])
    expected = [1]
    assert actual == expected


def test_merge1():
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_merge2():
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_merge3():
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_merge4():
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
