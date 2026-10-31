from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from utils.config import BASE_URL

class SearchPage(BasePage):
    URL = f"{BASE_URL}/search"
    CITY_INPUT = (By.XPATH, "//*[@id='city']")
    DATES_INPUT = (By.CSS_SELECTOR, "[id='dates']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    CAR_CARDS = (By.CSS_SELECTOR, ".car-card")


    def open_search_page(self):
        self.driver.get(self.URL)


    def fill_city(self, city):
        city_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CITY_INPUT)
        )
        city_input.click()
        city_input.clear()
        city_input.send_keys(city)
        WebDriverWait(self.driver, 5).until(
            lambda d: city_input.get_attribute("value") == city
        )

    def fill_dates(self, dates_interval):
        # закриваємо список підказок міста
        self.driver.find_element(*self.CITY_INPUT).send_keys(Keys.ESCAPE)

        date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DATES_INPUT)
        )
        try:
            date_input.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", date_input)

        # чекаємо, поки календар завантажиться
        WebDriverWait(self.driver, 15).until(
            lambda d: len(d.find_elements(
                By.CSS_SELECTOR, "#daterange-popover button.rdrDay")) > 0
        )

        start_date, end_date = [
            datetime.strptime(part.strip(), "%m/%d/%Y")
            for part in dates_interval.split(" - ")
        ]

        def select_day(target_date):
            day = str(target_date.day)
            popover = self.driver.find_element(By.ID, "daterange-popover")
            for button in popover.find_elements(By.CSS_SELECTOR, "button.rdrDay"):
                classes = button.get_attribute("class") or ""
                if (button.text.strip() == day
                        and "rdrDayDisabled" not in classes
                        and "rdrDayPassive" not in classes):
                    button.click()
                    return
            raise AssertionError(f"Day not found or unavailable: {target_date:%m/%d/%Y}")

        select_day(start_date)
        select_day(end_date)


    def fill_search_form(self, city, dates=None):
        self.open_search_page()
        self.fill_city(city)
        if dates:
            self.fill_dates(dates)

    def is_submit_enabled(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SUBMIT_BTN)
        )
        return button.is_enabled()

    def submit_search(self):
        city_value = self.driver.find_element(*self.CITY_INPUT).get_attribute("value")
        dates_value = self.driver.find_element(*self.DATES_INPUT).get_attribute("value")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BTN)
        )
        self.click(self.SUBMIT_BTN)

    def search_cars_steps(self, city, dates=None):
        self.fill_search_form(city, dates)
        self.submit_search()

    def is_car_results_present(self):
        try:
            WebDriverWait(self.driver, 20).until(
                lambda d: "Loading..." not in
                          d.find_element(By.TAG_NAME, "body").text
            )
        except TimeoutException:
            pass
        return len(self.driver.find_elements(*self.CAR_CARDS)) > 0
















