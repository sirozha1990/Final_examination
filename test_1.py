import time
from testpage import OperationsHelpers
import logging
import yaml
from selenium import webdriver
with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1():
    logging.info("Test1 starting")
    driver = webdriver.Chrome()
    testpage = OperationsHelpers(driver)
    testpage.go_to_site()
    testpage.enter_login("claudius.maximus")
    testpage.enter_pass("977547308c")
    testpage.click_login_button()
    assert testpage.get_user() == "Home"
def test_step2():
    logging.info("Test2 starting")
    driver = webdriver.Chrome()
    testpage = OperationsHelpers(driver)
    testpage.go_to_site()
    testpage.go_to_site()
    testpage.enter_login("claudius.maximus")
    testpage.enter_pass("977547308c")
    testpage.click_login_button()
    time.sleep(testdata['sleep_time'])
    testpage.click_about_link()
    time.sleep(testdata['sleep_time'])
    testpage.check_font_size()

