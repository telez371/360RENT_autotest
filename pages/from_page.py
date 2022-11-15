from time import sleep
from pages.base_page import BasePage
from locators.form_tests_locators import FromPageLocators as Locators
from capcha.form_capcha import read_capcha
from generator.generator import generated_person,generated_file

class Form_page(BasePage):
    def fill_fields_and_submit(self):
        person = generated_person()
        path = generated_file()
        self.element_is_visible(Locators.BTN_PRIMARY).click()
        self.element_is_visible(Locators.DROP_DOWN_REALTOR).click()
        self.element_is_visible(Locators.REGISTER).click()
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        CAPCHA_VALUE = read_capcha()
        self.element_is_visible(Locators.CAPCHA).send_keys(CAPCHA_VALUE)
        self.scroll_To(Locators.SCROLL)
        sleep(3)
        self.element_is_visible(Locators.REGISTER_BTN).click()


