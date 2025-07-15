import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)
    page.click_button('7')
    page.click_button('+')
    page.click_button('8')
    page.click_button('=')
    assert page.get_result()  # Ожидается "15" на экране
