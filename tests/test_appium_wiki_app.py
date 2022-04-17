from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

import pytest

from tools import CheckValues

LIST_OF_ATTRIBUTE_VALUES = ['Settings', 'Customize the feed', 'Support Wikipedia', 'About', 'Help']


class TestAppiumWikiApp:
    """It would better create framework,
    but there are just simple examples.
    So I decided not to create all structure
    for performing these tests."""

    @staticmethod
    @pytest.mark.skip(
        "Test doesn't work, something wrong with skip_button locator.")
    def test_skip_page(browser) -> None:
        skip_button = browser.find_element(By.ID, '//*[@text="SKIP"]')
        skip_button.click()

    @staticmethod
    @pytest.mark.skip(
        "The 'noReset' parameter is used in desired_capabilities.")
    def test_check_work_got_it_button(browser) -> None:
        """In this test case checking the 'clickability'
        a GOT IT button."""
        got_it_button = browser.find_element(
            by=By.ID,
            value="org.wikipedia:id/view_announcement_action_negative")
        got_it_button.click()

    @staticmethod
    # @pytest.mark.skip
    def test_setting_button(browser) -> None:
        """In this test performs checking
        attributes presence in setting panel."""
        setting_button = browser.find_element(
            by=By.ID,
            value='org.wikipedia:id/drawer_icon_menu')
        setting_button.click()
        CheckValues(browser).check_attribute_values(LIST_OF_ATTRIBUTE_VALUES)

    @staticmethod
    # @pytest.mark.skip
    @pytest.mark.parametrize("value", ["Python", "kakhkjhwqk2kj"])
    def test_search_field(browser, value) -> None:
        """In this test specified text is entered
        in the search field and
        search is performed. Enter value,
        compared answer with expected.
        Second test should fail."""

        search_wikipedia = browser.find_element(
            by=By.XPATH,
            value=f"//*[@text='Search Wikipedia']")
        assert search_wikipedia.is_displayed() is True,\
            "Element doesn't displayed."
        search_wikipedia.click()

        search_field = browser.find_element(
            by=By.ID,
            value='org.wikipedia:id/search_src_text')
        assert search_field.is_displayed() is True, \
            "Element doesn't displayed."
        search_field.send_keys(value)

        first_value_in_list = browser.find_element(
            by=By.ID,
            value='org.wikipedia:id/page_list_item_title')
        assert first_value_in_list.is_displayed() is True, \
            "Element doesn't displayed."
        assert value in first_value_in_list.text,\
            "Value text doesn't match."
