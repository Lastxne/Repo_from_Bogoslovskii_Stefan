import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-translate")
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_total_amount(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_to_cart("Sauce Labs Onesie")
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Ivan", "Ivanov", "123456")
    total = checkout.get_total()

    assert total.endswith("$58.29")
