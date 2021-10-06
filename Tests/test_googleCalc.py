import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Config.TestData import TestData
from Pages.MainGooglePage import MainGooglePage
from Pages.ResultsGooglePage import Calculator


def test_calc_by_input(browser):
    main_page = MainGooglePage(browser)
    result = Calculator(browser)
    main_page.go_to_site()
    main_page.enter_search_query(TestData.SEARCH_QUERY)
    main_page.click_on_the_dropdown_search_button()
    result.enter_calc_expression(TestData.CALC_EXPRESSION)
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()

    res = result.check_result()
    history = result.check_history()

    assert res == TestData.CORRECT_CALC_ANSWER
    assert history == TestData.NUMPAD_CALC_EXPRESSION


def test_calc_by_numpad(browser):
    main_page = MainGooglePage(browser)
    result = Calculator(browser)
    main_page.go_to_site()
    main_page.enter_search_query(TestData.SEARCH_QUERY)
    main_page.click_on_the_main_search_button()
    result.click_numpad(TestData.NUMPAD_CALC_EXPRESSION)

    res = result.check_result()
    history = result.check_history()

    assert res == TestData.CORRECT_CALC_ANSWER
    assert history == TestData.NUMPAD_CALC_EXPRESSION
