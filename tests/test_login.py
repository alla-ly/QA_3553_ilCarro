from pages.login_page import LoginPage

VALID_EMAIL = "anna123456@gmail.com"
VALID_PASSWORD = "Anna123456$"
INVALID_EMAIL = "anna123456gmail.com"
INVALID_PASSWORD = "as1"

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()
    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()

    assert login_page.is_logged() is True

#variant 2
def test_login_success_1(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()

    assert login_page.is_logged() is True

def test_login_with_wrong_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.get_email_error_text() == "Wrong email format"

def test_login_with_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.submit_login()

    assert login_page.get_error_message() == "Login or Password incorrect"
    login_page.click_ok_button()

def test_login_with_empty_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email("")
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.get_empty_email_error_text() == "Email is required"

def test_login_with_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password("")
    login_page.submit_login()

    assert login_page.get_empty_password_error_text() == "Password is required"