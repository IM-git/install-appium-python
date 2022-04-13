from appium import webdriver


"""These are the configuration keys from the virtual mobile,
we will use it for testing."""
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "X:\\D\\AQA\\appium_test\\app\\org.wikipedia-2.7.276-r-2019-03-27.apk"
}
command_executor = 'http://127.0.0.1:4723/wd/hub'


"""Here written url by default for connecting by virtual mobile.
This is the initialization of the driver as in Selenium."""
driver = webdriver.Remote(command_executor=command_executor,
                          desired_capabilities=desired_capabilities)
