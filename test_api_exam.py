import allure
import requests
from pydantic import ValidationError

import models

URL = "https://petstore.swagger.io/v2"


@allure.title("Post request status code")
@allure.tag("Good Post Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Creation")
def test_post_request_good():
    response = requests.post(URL + "/pet", json=models.PetPost.body).json()
    assert response.status_code == 200


@allure.title("Post request status code")
@allure.tag("Bad Post Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Creation")
def test_post_request_bad():
    response = requests.post(URL + "/pet", empty_tuple := []).json()
    assert response.status_code == 405


@allure.title("Post request status code")
@allure.tag("Empty Post Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Creation")
def test_post_request_bad():
    response = requests.post(URL + "/pet").json()
    assert response.status_code == 415


@allure.title("Put request status code")
@allure.tag("Change Status Request Good")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
def test_post_request_good():
    response = requests.put(URL + "/pet/578" + "status", "sold").json()
    assert response.status_code == 200


@allure.title("Put request status code")
@allure.tag("Change Status Request Bad")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
def test_post_request_good():
    response = requests.put(URL + "/pet/578" + "status", "lost").json()
    assert response.status_code == 405


@allure.title("Put request status code")
@allure.tag("Change Status Request Non-exist Pet")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
def test_post_request_good():
    response = requests.put(URL + "/pet/57854" + "status", "lost").json()
    assert response.status_code == 404


@allure.title("Put request status code")
@allure.tag("Change Status Request Bad ID Pet")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
def test_post_request_good():
    response = requests.put(URL + "/pet/5d8" + "status", "lost").json()
    assert response.status_code == 400


@allure.title("Get request status code")
@allure.tag("Find Sold Pet Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
def test_post_request_good():
    response = requests.get(URL + "/pet/578",).json()
    assert response.status_code == 200


@allure.title("Get request status code")
@allure.tag("Find Sold Pet Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
def test_post_request_good():
    response = requests.get(URL + "/pet/578/status", "sold").json()
    assert response.status_code == 400