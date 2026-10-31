
import logging
from data.user_data import create_user

from pages.registration_page import RegistrationPage

logger = logging.getLogger(__name__)


def test_registration_success(driver):#Оголошення функції автотесту
    # для успішної реєстрації.
    # Вона приймає фікстуру driver (екземпляр Selenium WebDriver),
    # яка відкриває та керує браузером.
    registration_page = RegistrationPage(driver)#Створюється екземпляр класу Page Object RegistrationPage
    user = create_user() #Викликається допоміжна функція-фабрика create_user(), яка генерує об'єкт користувача з
    # унікальними даними (ім'я, прізвище, email, пароль).


    registration_page.open_registration_form()#Відкриття форми реєстрації.
    registration_page.fill_registration_form(user)#Заповнення полів форми реєстрації
    registration_page.check_policy()#Встановлення галочки згоди з політикою конфіденційності.

    registration_page.submit_registration()#Натискання на кнопку відправки форми реєстрації
    logger.info("Test: test registration success")

    assert registration_page.confirmation_text() == "Registered"#перевіряється, чи заголовок підтвердження дорівнює точній фразі
    assert registration_page.confirmation_message() == "You are logged in success"#перевіряється, чи основний текст повідомлення про успішний вхід відповідає фразі
    registration_page.close_window()#Закриття діалогового/модального вікна з повідомленням про успішну реєстрацію.


def test_registration_with_empty_name(driver):
    logger.info("Test: test registration with empty name started")
    registration_page = RegistrationPage(driver)#Створення екземпляра класу RegistrationPage
    user = create_user(name = "")

    registration_page.open_registration_form()#Відкриття форми реєстрації.
    registration_page.fill_registration_form(user)#Спроба заповнити форму (поле імені залишиться порожнім
    registration_page.check_policy()#Встановлення галочки згоди з політикою конфіденційності.

    registration_page.submit_registration()#Спроба натиснути кнопку відправки форми.

    assert registration_page.error_message_text() == "Name is required"#перевіряється, чи з'явилося під полем імені
    # повідомлення про помилку з текстом
    assert registration_page.submit_button_disabled()#еревіряється, чи кнопка відправки форми залишається заблокованою


def test_registration_with_empty_last_name(driver):
    logger.info("Test: test registration with empty last_name")
    registration_page = RegistrationPage(driver)

    user = create_user(last_name="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Last name is required"
    assert registration_page.submit_button_disabled()



def test_registration_with_wrong_email(driver):
    logger.info("Test: test registration with wrong email")
    registration_page = RegistrationPage(driver)
    user = create_user(email="tony_mollygmail.com")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Wrong email format"
    assert registration_page.submit_button_disabled()



def test_registration_with_empty_email(driver):
    logger.info("Test: test registration with empty email")
    registration_page = RegistrationPage(driver)
    user = create_user(email="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Email is required"
    assert registration_page.submit_button_disabled()


def test_registration_with_wrong_password(driver):
    logger.info("Test: test registration with wrong password")
    registration_page = RegistrationPage(driver)
    user = create_user(password="P123$")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password must contain minimum 6 symbols"
    assert registration_page.submit_button_disabled()


def test_registration_with_empty_password(driver):
    logger.info("Test: test registration with empty password")
    registration_page = RegistrationPage(driver)

    user = create_user(password="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password is required"
    assert registration_page.submit_button_disabled()


def test_registration_without_check_box(driver):
    logger.info("Test: test registration without check box")
    registration_page = RegistrationPage(driver)
    user = create_user()

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "You must accept the terms"
    assert registration_page.submit_button_disabled()
