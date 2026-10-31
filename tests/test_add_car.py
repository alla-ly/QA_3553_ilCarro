import os.path
from pathlib import Path
import pytest
from selenium.webdriver.common.by import By

import logging

logger = logging.getLogger(__name__)

from data.car_data import create_car
from pages.add_car_page import AddCarPage


PHOTO_PATH = os.path.join(
    os.path.dirname(__file__),"..","resources","images","img.png"
)

def test_add_car_success(authenticated_driver):
    """Позитивний тест: успішне додавання автомобіля з усіма заповненими полями"""
    logger.info("Test: test add car success started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

#---NEGATIVE TESTS__


def test_add_car_duplicate_serial_number_rejected(authenticated_driver):
    """Негативний тест: спроба додати авто з вже існуючим серійним номером"""
    logger.info("Test: test add car duplicate serial number started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    # Перше додавання
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()
    # Повторне додавання того ж авто
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    logger.warning("Unusual behavior")

    assert car_page.error_message_text() == "Failed to submit car"

@pytest.mark.smoke
def test_add_car_empty_city_rejected(authenticated_driver):
    logger.info("Test: test add car empty city started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.city = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.error_message_text() == "Failed to submit car"


def test_add_car_empty_make_rejected(authenticated_driver):
    """Негативний тест: спроба додати авто з порожнім полем Manufacture"""
    logger.info("Test: test add car success started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.manufacture = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()
    logger.info("Testing empty edited empty make")

    assert car_page.get_field_error("manufacture") == "Required"


@pytest.mark.smoke
def test_add_car_empty_model_rejected(authenticated_driver):
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.model = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()
    logger.info("Testing empty edited empty model")

    assert car_page.get_field_error("model") == "Required"


@pytest.mark.regression
def test_add_car_empty_year_rejected(authenticated_driver):
    logger.info("Test: test add car empty year started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.year = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.get_field_error("year") == "Required"


def test_add_car_empty_fuel_rejected(authenticated_driver):
    logger.info("Test: test add car empty fuel started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.fuel = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.is_submit_button_disabled()

@pytest.mark.smoke
def test_add_car_empty_gear_rejected(authenticated_driver):
    logger.info("Test: test add car empty gear started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.gear = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.is_submit_button_disabled()

def test_add_car_empty_wheels_drive_rejected(authenticated_driver):
    logger.info("Test: test add car empty wheels drive started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.wheels_drive = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.is_submit_button_disabled()


@pytest.mark.smoke
@pytest.mark.regression
def test_add_car_empty_doors_accepted(authenticated_driver):
    logger.info("Test: test add car empty doors accepted started")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.doors = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)

    assert not car_page.is_submit_button_disabled()



def test_add_car_empty_seats_rejected(authenticated_driver):
    logger.info("Test: test add car empty seats")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.seats = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.is_submit_button_disabled()


@pytest.mark.regression
def test_add_car_negative_seats_rejected(authenticated_driver):
    logger.info("Test: test add car negative seats")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.seats = "-2"
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.is_submit_button_disabled()



def test_add_car_empty_car_class_rejected(authenticated_driver):
    logger.info("Test: test add car empty car class")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.car_class = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.get_field_error("carClass") == "Required"



def test_add_car_empty_car_registration_number_rejected(authenticated_driver):
    logger.info("Test: test add car empty car")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.serial_number = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.get_field_error("serialNumber") == "Required"



def test_add_car_empty_price_rejected(authenticated_driver):
    logger.info("Test: test add car empty price")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.price_per_day = ""
    car_page.open_car_form()
    car_page.fill_car_form(car)
    car_page.submit_car()

    assert car_page.get_field_error("pricePerDay") == "Required"


@pytest.mark.xfail(reason="BUG-127: Test add car negative price rejected")
def test_add_car_negative_price_rejected(authenticated_driver):
    logger.info("Test: test add car negative price")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PATH)
    car.price_per_day = "-50"
    car_page.open_car_form()
    car_page.fill_car_form(car)

    assert car_page.is_submit_button_disabled()


@pytest.mark.regression
def test_add_car_without_photo(authenticated_driver):
    logger.info("Test: test add car without photo")
    car_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=None)

    car_page.open_car_form()
    car_page.fill_car_form(car)

    assert not car_page.is_submit_button_disabled()





































