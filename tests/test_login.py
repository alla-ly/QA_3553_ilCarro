from data.user_data import existing_user
from pages.login_page import LoginPage
import  pytest
import logging
import allure
WRONG_EMAIL = "margogmail.com"

logger = logging.getLogger(__name__)


@allure.feature("Login")
def test_login_success(driver):
    logger.info("Test: test login success started")
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.confirmation_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True


def test_login_wrong_email(driver):
    logger.info("Test: test login wrong email started")
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(WRONG_EMAIL)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.error_message_text()=="Wrong email format"
    assert login_page.submit_button_disabled()


@pytest.mark.parametrize("email, password", [
    ("", "Pass123$"),
    ("", "Pass456$"),
])
def test_login_empty_email(driver,email, password):
    logger.info("Test: test login empty email started")
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email("")
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.error_message_text()=="Email is required"
    assert login_page.submit_button_disabled()

@allure.feature("Login")
@allure.story("Wrong password")
@allure.title("Вхід із неправильним паролем")
@pytest.mark.parametrize("email, password"
, [
    ("a@gmail.com", "Pass123$"),
    ("b@gmail.com", "Pass456$"),
])
def test_login_wrong_password(driver, email, password):
    logger.info("Test: test login wrong password started")
    login_page = LoginPage(driver)
    with allure.step("Open login form"):
        login_page.open_login_form()

    login_page.open_login_form()
    login_page.fill_email(email)
    login_page.fill_password(password)
    with allure.step("Fill wrong password"):
        login_page.fill_password(password)
    login_page.submit_login()

    assert login_page.confirmation_text()== "Login failed"
    assert login_page.confirmation_message()== '"Login or Password incorrect"'


@allure.story("Empty password")
def test_login_empty_password(driver):
    logger.info("Test: test login empty password started")
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password("")
    login_page.submit_login()

    logger.warning("Unusual behavior")
    assert login_page.error_message_text()=="Password is required"
    assert login_page.submit_button_disabled()
