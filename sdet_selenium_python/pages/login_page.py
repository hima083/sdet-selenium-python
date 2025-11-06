from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    USER = (By.ID, "username")
    PASS = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button.radius")
    FLASH = (By.ID, "flash")

    def load(self):
        self.open(self.URL)

    def login(self, username, password):
        self.find(*self.USER).send_keys(username)
        self.find(*self.PASS).send_keys(password)
        self.find(*self.SUBMIT).click()

    def success_message(self):
        return self.find(*self.FLASH).text
