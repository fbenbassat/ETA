import time

from Pages.ProductsPage import ProductsPage
from Pages.YourCartPage import YourCartPage


class Test6:

    def test_add_product_to_cart(self, login_saucedemo):
        products_page = ProductsPage(driver=login_saucedemo.driver)
        product_name = products_page.add_random_product_to_cart()
        assert products_page.get_card_number() == "1", "Carrinho não contém 1 produto!"
        products_page.open_cart_page()
        your_cart_page = YourCartPage(driver=products_page.driver)
        assert your_cart_page.is_your_cart_page(), 'Your Cart page not found!'
        assert your_cart_page.has_product_in_cart(name=product_name), 'Produto não encontrado!'

