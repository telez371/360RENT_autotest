from pages.from_page import Form_page



class TestFormPage:

    def test_form(self, driver):
        forme_page = Form_page(driver, "https://360rent.club/ru/")
        forme_page.open()
        forme_page.fill_fields_and_submit()


