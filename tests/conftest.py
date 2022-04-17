import pytest
from appium import webdriver


IMPLICITLY_WAIT_TIME = 5

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
    "app": "X:\\D\\AQA\\install-appium-python\\app\\org.wikipedia-2.7.276-r-2019-03-27.apk",
    "noReset": True
}
command_executor = 'http://127.0.0.1:4723/wd/hub'


@pytest.fixture(scope='function')
def browser():
    """Initialization driver.
    Here written command_executor(url) by default
    for connecting by virtual mobile.
    This is the initialization of the driver as in Selenium."""
    driver = webdriver.Remote(command_executor=command_executor,
                              desired_capabilities=desired_capabilities)
    driver.implicitly_wait(IMPLICITLY_WAIT_TIME)
    yield driver
    driver.quit()
