import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    NAV_REGISTRATION_BTN = (By.CSS_SELECTOR, "[href='/register']")
    NAME_INPUT = (By.CSS_SELECTOR, "[name='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    YALLA_BTN = (By.XPATH, "//button[text()='Y’alla!']")
    CHECK_BOX = (By.ID,"terms-of-use")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "p")
    OK_BTN = (By.XPATH, "//*[text()='OK']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def open_registration_form(self):
        self.click(self.NAV_REGISTRATION_BTN)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )

    def fill_name(self, name):
        self.fill(self.NAME_INPUT,name)

    def fill_last_name(self, last_name):
        self.fill(self.LAST_NAME_INPUT,last_name)

    def fill_email(self, email):
        self.fill(self.EMAIL_INPUT,email)

    def fill_password(self, password):
        self.fill(self.PASSWORD_INPUT,password)

    def submit_registration(self):
        self.click(self.YALLA_BTN)

    def check_policy(self):
        self.click(self.CHECK_BOX)

    def fill_registration_form(self, user):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_password(user.password)

    def confirmation_text(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
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

    def error_message_text(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def submit_button_disabled(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.YALLA_BTN)
        )
        return element.get_attribute("disabled") is not None




























