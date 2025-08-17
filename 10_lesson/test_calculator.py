import pytest
import allure
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Test Calculator Addition")
@allure.description(
    "This test verifies the addition functionality of the calculator."
)
@allure.feature("Calculator")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)

    with allure.step("Click on 7"):
        page.click_button('7')

    with allure.step("Click on +"):
        page.click_button('+')

    with allure.step("Click on 8"):
        page.click_button('8')

    with allure.step("Click on ="):
        page.click_button('=')

    with allure.step("Verify result is 15"):
        assert page.get_result()  # Ожидается "15" на экране
