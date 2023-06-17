
class Test1:

    def test_click_login_btn(self, open_login_page):
        login_page = open_login_page
        login_page.click_login_btn()
        assert login_page.is_url_login(), "Aplicação não está na pagina de login!"
        assert login_page.has_login_message_error(), "Mensagem de erro inválida!"



