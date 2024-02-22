import logging
import requests
import yaml

with open("testdata.yaml", "r") as f:
    data = yaml.safe_load(f)


def user_loging(token):
    resource = requests.get("https://test-stand.gb.ru/api/users/profile/21354",
                            headers={"X-Auth-Token": token})

    return resource.json()


def test_1(test_login):
    logging.info("Test1 API: logging user == user ")
    user = user_loging(test_login)['id']
    assert user == 21354