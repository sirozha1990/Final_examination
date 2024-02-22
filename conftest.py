import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browserr = testdata['browser']

@pytest.fixture()
def browser():
    if browserr == 'chrome':
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError
    yield driver
    driver.quit()
@pytest.fixture()
def test_login():
    response = requests.post(url="https://test-stand.gb.ru/gateway/login",
                             data={'username': testdata['login'], 'password': testdata['passwd']})

    # if response.status_code == 200:
    token = response.json()['token']
    return token