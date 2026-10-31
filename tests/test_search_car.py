
import pytest
from pages.search_page import SearchPage
from datetime import date, timedelta

import logging

logger = logging.getLogger(__name__)

@pytest.mark.xfail(reason="BUG-123: Search car")
def test_search_car_success(driver):
    logger.info("Test: test search car success started")
    search_page = SearchPage(driver)

    start = date.today() + timedelta(days=1)
    end = date.today() + timedelta(days=3)
    start_str = start.strftime("%m/%d/%Y")
    end_str = end.strftime("%m/%d/%Y")

    logger.warning("Unusual behavior")
    search_page.search_cars_steps(city="Tel Aviv", dates=f"{start_str} - {end_str}")

    logger.error("Error: %s")
    assert search_page.is_car_results_present() is True

@pytest.mark.xfail(reason="BUG-124: Search car empty city")
def test_search_car_empty_city_rejected(driver):
    logger.info("Test: test search car empty city rejected started")
    search_page = SearchPage(driver)
    start = date.today() + timedelta(days=1)
    end = date.today() + timedelta(days=3)

    logger.warning("Unusual behavior")
    search_page.fill_search_form(
        city="",
        dates=f"{start:%m/%d/%Y} - {end:%m/%d/%Y}"
    )

    logger.error("Error: %s")
    assert search_page.is_submit_enabled() is False