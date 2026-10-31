import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LoginPage(BasePage):
    NAV_LOGIN_BTN = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    YALLA_BTN = (By.XPATH, "//button[text()='Y’alla!']")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "p")
    OK_BTN = (By.XPATH, "//*[text()='OK']")
    LOG_OUT_BTN = (By.XPATH, "//*[text()='Log out']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def open_login_form(self):
        self.click(self.NAV_LOGIN_BTN)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )

    def fill_email(self, email):
        self.fill(self.EMAIL_INPUT,email)

    def fill_password(self, password):
        self.fill(self.PASSWORD_INPUT,password)

    def submit_login(self):
        self.click(self.YALLA_BTN)

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()

    def confirmation_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
           EC.visibility_of_element_located(self.CONFIRMATION_TEXT))
        return element.text


    def confirmation_message(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_MESSAGE))
        return element.text

    def close_window(self):
        self.click(self.OK_BTN)

    def is_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.LOG_OUT_BTN)
            )
            return True
        except TimeoutException:
            return False

    def error_message_text(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def submit_button_disabled(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.YALLA_BTN)
        )
        return element.get_attribute("disabled") is not None











