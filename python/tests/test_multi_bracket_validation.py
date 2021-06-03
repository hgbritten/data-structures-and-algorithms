import pytest
from code_challenges.multi_bracket_validation.multi_bracket_validation import (
    multi_bracket_validation,
)


def test_multi():
    assert multi_bracket_validation


def test_string():
    actual = multi_bracket_validation("dog")
    expected = True
    assert actual == expected


def test_string2():
    actual = multi_bracket_validation("(dog)")
    expected = True
    assert actual == expected


def test_string3():
    actual = multi_bracket_validation("({[dog]})")
    expected = True
    assert actual == expected


def test_string4():
    actual = multi_bracket_validation("({[dog]}))")
    expected = False
    assert actual == expected


def test_string5():
    actual = multi_bracket_validation(")({[dog]})")
    expected = False
    assert actual == expected
