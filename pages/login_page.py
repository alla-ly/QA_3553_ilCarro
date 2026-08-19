import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    NAV_LOGIN_BTN = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    YALLA_BTN = (By.XPATH, "//button[text()='Y’alla!']")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")

    OK_BTN = (By.XPATH, "//*[text()='OK' or text()='OK' ]")
    LOG_OUT_BTN = (By.XPATH,"//*[text()='Log out']")
    EMAIL_ERROR_TEXT = (By.XPATH, "//div[@class='error']")

    ERROR_TITLE = (By.XPATH,"//*[@class='modal-content']//h2")
    ERROR_MESSAGE = (By.XPATH,"//*[@class='modal-content']//p")

    EMPTY_FIELD_EMAIL = (By.XPATH, "//*[text()='Email is required']")
    EMPTY_FIELD_PASSWORD = (By.XPATH,"//*[text()='Password is required']")


    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.NAV_LOGIN_BTN).click()
        time.sleep(2)

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.YALLA_BTN).click()

#variant 2
    def login(self,email,password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()

    def login_success_text(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT)
        )
        return element.text

    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

    def is_logged(self):
        try:
            WebDriverWait(self.driver,timeout=5).until(
                EC.visibility_of_element_located(self.LOG_OUT_BTN)
            )
            return True
        except TimeoutException:
            return False

    def get_email_error_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.EMAIL_ERROR_TEXT)
        )
        return element.text

    def get_error_message(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text.replace('"', '').strip()

    def click_ok_button(self):
        ok_btn = WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(self.OK_BTN)
        )
        ok_btn.click()

    def get_empty_email_error_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.EMPTY_FIELD_EMAIL)
        )
        return element.text

    def get_empty_password_error_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.EMPTY_FIELD_PASSWORD)
        )
        return element.text














