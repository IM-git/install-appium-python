from selenium.webdriver.common.by import By


class CheckValues:

    def __init__(self, browser):
        self.browser = browser

    def check_attribute_values(self, list_values):
        for value in list_values:
            answer_value = self.browser.find_element(
                by=By.XPATH,
                value=f"//*[@text='{value}']")
            assert bool(answer_value) is True, "Value text doesn't match."
