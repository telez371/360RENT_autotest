from selenium.webdriver.common.by import By


class FromPageLocators:

    BTN_PRIMARY = (By.CSS_SELECTOR, "#agree")
    DROP_DOWN_REALTOR = (By.CSS_SELECTOR, "#navbarDropdownRealtor")
    REGISTER = (By.CSS_SELECTOR, '.dropdown-menu  [href="https://360rent.club/ru/realtor/signup"]')
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    CAPCHA = (By.CSS_SELECTOR, "input[name='captcha']")
    REGISTER_BTN = (By.CSS_SELECTOR, "[type='submit']")
    SCROLL = "window.scrollTo(0,200)"

