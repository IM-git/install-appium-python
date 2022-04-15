from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time

"""These are the configuration keys from the virtual mobile,
we will use it for testing.
The 'app' this a just a folder with code is locate on the specified path,
the location may differ.
More information: https://pypi.org/project/Appium-Python-Client/.
Added 'noReset'(do not clear app data) for skip first page
with languages selection."""

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "X:\\D\\AQA\\appium_test\\app\\org.wikipedia-2.7.276-r-2019-03-27.apk",
    "noReset": True
}
command_executor = 'http://127.0.0.1:4723/wd/hub'

"""Here written url by default for connecting by virtual mobile.
This is the initialization of the driver as in Selenium."""
# driver = webdriver.Remote(command_executor=command_executor,
#                           desired_capabilities=desired_capabilities)


class TestAppiumWikiApp:

    @staticmethod
    @pytest.mark.skip(
        "The 'noReset' parameter is used in desired_capabilities.")
    def test_check_work_got_it_button(browser):
        """In this test case checking the 'clickability'
        a GOT IT button."""
        got_it_button = browser.find_element(
            By.ID, value="org.wikipedia:id/view_announcement_action_negative")
        got_it_button.click()

    @staticmethod
    def test_setting_button(browser):
        """In this test performs checking
        attributes presence in setting panel."""
        setting_button = browser.find_element(
            By.ID, value='org.wikipedia:id/drawer_icon_menu')
        setting_button.click()

        #   Created a loop, because assert statement had dub-code.
        #   Need to cheap this loop in separate function and file in the tools folder.
        LIST_OF_ATTRIBUTE_VALUES = ['Settings', 'Customize the feed', 'Support Wikipedia', 'About', 'Help']
        for value in LIST_OF_ATTRIBUTE_VALUES:
            answer_value = browser.find_element(By.XPATH, f"//*[@text='{value}']")
            assert bool(answer_value) is True, "####Value text doesn't match.#####"
