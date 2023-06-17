import pytest

from Pages.ProductsPage import ProductsPage


class Test2:

    @pytest.mark.parametrize('all_browser', ['chrome', 'safari', 'firefox'])
    def test_efetuar_login(self, open_login_page_all_browser):
        login_page = open_login_page_all_browser
        login_page.efetuar_login()

        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_url_products(), 'URL da página de produtos não encontrada!'
        assert products_page.is_products_title(), 'Título da página de produtos é diferente!'
        assert products_page.has_products_in_list(), 'Lista de produtos não encontrada!'

