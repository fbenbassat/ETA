import pytest

from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


@pytest.fixture()
def open_login_page():
    login_page = LoginPage()
    yield login_page
    login_page.save_screenshot_page()
    login_page.close()

@pytest.fixture()
def login_saucedemo(open_login_page):
    login_page = open_login_page
    login_page.efetuar_login()
    yield login_page

@pytest.fixture()
def one_product_in_cart(login_saucedemo):
    products_page = ProductsPage(driver=login_saucedemo.driver)
    products_page.add_random_product_to_cart()
    yield products_page


