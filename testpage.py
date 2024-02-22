from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_ABOUT_BTN = (By.XPATH, """// *[ @ id = "app"] / main / nav / ul / li[1] / a""")
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_USER_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/a/span""")





class OperationsHelpers(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_CONTACT_BTN = None

    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user(self):
        logging.info("User")
        user = self.find_element(TestSearchLocators.LOCATOR_USER_FIELD, time=2)
        text = user.text
        return text

    def click_about_link(self):
        logging.info("Click button About")
        self.find_element(TestSearchLocators.LOCATOR_ABOUT_BTN).click()


    def check_font_size(self):
        font_size = self.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div/h1').value_of_css_property(
            "font-size")
        if font_size == "32px":
            logging.info("Font size is 32px")
        else:
            logging.error("Font size is not 32px, actual size is {}".format(font_size))
        return font_size