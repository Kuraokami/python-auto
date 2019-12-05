# coding=utf-8
"""SauceDemo feature tests."""
from .page_objects import LoginPage
from selenium import webdriver
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)

login = None
driver = webdriver.Chrome()


@scenario('./features/test_login.feature', 'I can login with valid user')
def test_i_can_login_with_valid_user():
    pass


@given(parsers.parse('I enter {name} page'))
def i_enter_da_page(name):
    global login
    global driver
    login = LoginPage.LoginPage(driver)


@when('I try to login with standardUser')
def i_try_to_login_with_standarduser():
    global login
    login.standard_login()
    time.sleep(3)


@then('I can see the products page')
def i_can_see_the_products_page():
    global driver
    assert "inventory" in driver.current_url
    driver.close()
