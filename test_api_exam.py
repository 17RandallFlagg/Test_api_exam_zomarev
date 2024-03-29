import allure
import requests
from models import Pet
import request_validation
from conftest import TEST_ID_FOR_PET

URL = "https://petstore.swagger.io/v2"


@allure.title("Post request status code")
@allure.tag("Good Post Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Creation")
@allure.description("Expected request")
def test_post_request_good(body_post_request):
    response = requests.post(URL + "/pet", json=body_post_request)
    res_js = response.json()
    with allure.step("Check Status code"):
        assert response.status_code == 200
    assert request_validation.validation(res_js, Pet)


@allure.title("Post request status code")
@allure.tag("Bad Post Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Creation")
@allure.description("Request with empty tuple")
def test_post_request_bad():
    empty_tuple = []
    response = requests.post(URL + "/pet", empty_tuple)
    with allure.step("Check Status code"):
        assert response.status_code == 405


@allure.title("Post request status code")
@allure.tag("Empty Post Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Creation")
@allure.description("Total empty request")
def test_post_empty_request():
    response = requests.post(URL + "/pet", None)
    with allure.step("Check Status code"):
        assert response.status_code == 415


@allure.title("Put request status code")
@allure.tag("Change Status Request Good")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Change status of pet to 'sold'")
def test_put_status_request_good(body_put_status_change_request):
    response = requests.put(URL + "/pet", json=body_put_status_change_request)
    res_js = response.json()
    with allure.step("Check Status code"):
        assert response.status_code == 200
    assert request_validation.validation(res_js, Pet)


@allure.title("Put request status code")
@allure.tag("Change Status Request Bad")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Change status of pet to 'lost'(non-existent status)")
def test_put_status_request_bad(body_put_status_change_request_wrong_status):
    response = requests.put(URL + "/pet", json=body_put_status_change_request_wrong_status)
    with allure.step("Check Status code"):
        assert response.status_code == 405


@allure.title("Put request status code")
@allure.tag("Change Status Request Non-exist Obj")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Try to change non-existent object (second name)")
def test_put_status_request_non_exist_obj(body_put_status_change_request_wrong_obj):
    response = requests.put(URL + "/pet", json=body_put_status_change_request_wrong_obj)
    with allure.step("Check Status code"):
        assert response.status_code == 404


@allure.title("Put request status code")
@allure.tag("Change Status Request Bad ID Pet")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Try to change pet with negative ID")
def test_put_status_request_bad_id_pet(body_put_status_change_request_wrong_id):
    response = requests.put(URL + "/pet", json=body_put_status_change_request_wrong_id)
    with allure.step("Check Status code"):
        assert response.status_code == 400


@allure.title("Get request status code")
@allure.tag("Find Sold Pet Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Search uploaded pet with status sold")
def test_get_request_my_pet_is_sold():
    response = requests.get(URL + "/pet/findByStatus?status=sold")
    res_js = response.json()
    with allure.step("Check Status code"):
        assert response.status_code == 200
    for pet in res_js:
        assert request_validation.validation(pet, Pet)
    in_list_sold_my_pet = 0
    with allure.step("Check sold status for my pet"):
        for pet in response:
            if pet[0] == TEST_ID_FOR_PET:
                in_list_sold_my_pet += 1
        assert in_list_sold_my_pet == 1


@allure.title("Get request status code")
@allure.tag("Find Lost Pet Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Search pets with status non-existent status 'lost'")
def test_get_request_lost():
    response = requests.get(URL + "/pet/findByStatus?status=lost")
    with allure.step("Check Status code"):
        assert response.status_code == 400


@allure.title("Delete request status code")
@allure.tag("Delete Pet Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Delete uploaded pet")
def test_delete_request():
    response = requests.delete(URL + "/pet/" + f"{TEST_ID_FOR_PET}")
    with allure.step("Check Status code"):
        assert response.status_code == 200


@allure.title("Delete request status code")
@allure.tag("Try To Delete Deleted Pet Request")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Try to delete non-existent pet")
def test_delete_request_repeat():
    response = requests.delete(URL + "/pet/" + f"{TEST_ID_FOR_PET}")
    with allure.step("Check Status code"):
        assert response.status_code == 404


@allure.title("Delete request status code")
@allure.tag("Try To Delete Pet With Failed ID")
@allure.label("owner", "aleksander.zomarev@gcore.lu")
@allure.epic("Test API")
@allure.feature("Change")
@allure.description("Try to delete a pet with incorrect ID")
def test_delete_request_wrong_id():
    response = requests.delete(URL + "/pet/wcw")
    with allure.step("Check Status code"):
        assert response.status_code == 400
