from code_challenges.quick_sort.quick_sort import quick_sort
import pytest


# @pytest.mark.skip("pending")
def test_quick_sort():
    assert quick_sort


def test_quick_sort1():
    actual = quick_sort([8, 4, 23, 42, 16, 15], 0, 5)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_quick_sort2():
    actual = quick_sort([20, 18, 12, 8, 5, -2], 0, 5)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_quick_sort3():
    actual = quick_sort([5, 12, 7, 5, 5, 7], 0, 5)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_quick_sort4():
    actual = quick_sort([2, 3, 5, 7, 13, 11], 0, 5)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
