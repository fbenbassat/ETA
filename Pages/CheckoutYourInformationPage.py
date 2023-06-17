from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CheckoutYourInformationPage(PageObject):

    url_checkout = 'https://www.saucedemo.com/checkout-step-one.html'
    text_checkout_title = 'Checkout: Your Information'
    id_continue_btn = 'continue'
    class_error_message = 'error-message-container'
    text_error_first_name = 'Error: First Name is required'

    def __init__(self, driver):
        super(CheckoutYourInformationPage, self).__init__(driver=driver)

    def is_checkout_your_information_page(self):
        return self.is_page(url=self.url_checkout, title_text=self.text_checkout_title)

    def click_continue(self):
        self.driver.find_element(By.ID, self.id_continue_btn).click()

    def has_first_name_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_error_message).text == self.text_error_first_name
