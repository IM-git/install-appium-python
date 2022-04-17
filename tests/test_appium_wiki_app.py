from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys

import pytest
import requests
import time

"""These are the configuration keys from the virtual mobile,
we will use it for testing.
The 'app' this a just a folder with code is locate on the specified path,
the location may differ.
More information: https://pypi.org/project/Appium-Python-Client/.
Added 'noReset'(do not clear app data) for skip first page
with languages selection."""
# desired_capabilities = {
#     "platformName": "Android",
#     "platformVersion": "9",
#     "deviceName": "Android Emulator",
#     "app": "X:\\D\\AQA\\appium_test\\app\\org.wikipedia-2.7.276-r-2019-03-27.apk",
#     "noReset": True
# }
# command_executor = 'http://127.0.0.1:4723/wd/hub'

"""Here written url by default for connecting by virtual mobile.
This is the initialization of the driver as in Selenium."""
# driver = webdriver.Remote(command_executor=command_executor,
#                           desired_capabilities=desired_capabilities)


class TestAppiumWikiApp:
    """It would better create framework,
    but there are just simple examples.
    So I decided not to create all structure
    for performing these tests."""

    @staticmethod
    def test_skip_page(browser):
        skip_button = browser.find_element(By.CLASS_NAME, 'android.widget.TextView')
        skip_button.click()

    @staticmethod
    @pytest.mark.skip(
        "The 'noReset' parameter is used in desired_capabilities.")
    def test_check_work_got_it_button(browser) -> None:
        """In this test case checking the 'clickability'
        a GOT IT button."""
        print(f'#######{id(browser)}#######')
        got_it_button = browser.find_element(
            By.ID, value="org.wikipedia:id/view_announcement_action_negative")
        got_it_button.click()

    @staticmethod
    @pytest.mark.skip
    def test_setting_button(browser) -> None:
        """In this test performs checking
        attributes presence in setting panel."""
        print(f'#######{id(browser)}#######')
        status_code = requests.get(url='http://127.0.0.1:4723/wd/hub').status_code
        print(status_code)
        setting_button = browser.find_element(
            By.ID, value='org.wikipedia:id/drawer_icon_menu')
        setting_button.click()

        #   Created a loop, because assert statement had dub-code.
        #   Need to cheap this loop in separate function and file in tools folder.
        LIST_OF_ATTRIBUTE_VALUES = ['Settings', 'Customize the feed', 'Support Wikipedia', 'About', 'Help']
        for value in LIST_OF_ATTRIBUTE_VALUES:
            answer_value = browser.find_element(
                By.XPATH, f"//*[@text='{value}']")
            assert bool(answer_value) is True, "Value text doesn't match."

    @staticmethod
    @pytest.mark.skip
    def test_search_field(browser) -> None:
        """In this test specified text is entered
        in the search field and
        search is performed. Enter value,
        compared answer with expected."""

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
        search_field.send_keys("Python")

        first_value_in_list = browser.find_element(
            by=By.ID,
            value='org.wikipedia:id/page_list_item_title')
        assert first_value_in_list.is_displayed() is True, \
            "Element doesn't displayed."
        assert "Python" in first_value_in_list.text,\
            "Value text doesn't match."
