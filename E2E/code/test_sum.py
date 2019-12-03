# coding=utf-8
"""I can sum things up feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)

result = 0
first = 0
second = 0


@scenario('features/sum.feature', 'I can sum two numbers')
def test_i_can_sum_two_numbers():
    """I can sum two numbers."""


@given(parsers.parse('I have {param:d}'))
def i_have_3(param):
    global first
    first = param


@when(parsers.parse('I sum {param:d}'))
def i_sum_2(param):
    global second
    global result
    second = param
    result = first + second


@then(parsers.parse('I have {param:d} as result'))
def i_have_5_as_result(param):
    assert result == param
