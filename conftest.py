import re
from datetime import datetime
from pathlib import Path
import allure
import pytest

from selenium import webdriver
from data.user_data import existing_user
from pages.login_page import LoginPage

from utils.config import BASE_URL
import logging
from selenium import webdriver

from utils.config import BASE_URL

logger = logging.getLogger(__name__)
SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    logger.info("Starting browser session: %s (headless=%s)", browser, headless)

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    if headless:
        driver.set_window_size(1920, 1080)
    else:
        driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    logger.info("Closing browser session")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Browser to run tests in: chrome, firefox or edge",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run the browser without a visible window",
    )


@pytest.fixture(scope="function")
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()
    login_page.close_window()   # закриває вікно «You are logged in success»

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture(autouse=True)
def save_screenshot_on_failure(request, driver):
    yield
    setup_report = getattr(request.node, "rep_setup", None)
    call_report = getattr(request.node, "rep_call", None)
    failed = (setup_report and setup_report.failed) or (call_report and call_report.failed)
    if not failed:
        return

    try:
        SCREENSHOTS_DIR.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        safe_name = re.sub(r'[<>:"/\\|?*]', "_", request.node.name)
        path = SCREENSHOTS_DIR / f"{safe_name}_{stamp}.png"
        logger.error("Test failed: %s", request.node.nodeid)
        if driver.save_screenshot(str(path)):
            allure.attach.file(str(path), name="screenshot",
                               attachment_type=allure.attachment_type.PNG)
    except Exception as error:
        logger.warning("Could not save screenshot: %s", error)


