import pytest
TEST_ID_FOR_PET = 578


@pytest.fixture(scope="function")
def body_post_request():
    body = {
      "id": TEST_ID_FOR_PET,
      "category": {
        "id": 423,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 647,
          "name": "string"
        }
      ],
      "status": "available"
    }
    return body


@pytest.fixture(scope="function")
def body_put_status_change_request():
    body = {
      "id": TEST_ID_FOR_PET,
      "category": {
        "id": 423,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 647,
          "name": "string"
        }
      ],
      "status": "sold"
    }
    return body


@pytest.fixture(scope="function")
def body_put_status_change_request_wrong_status():
    body = {
      "id": TEST_ID_FOR_PET,
      "category": {
        "id": 423,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 647,
          "name": "string"
        }
      ],
      "status": "lost"
    }
    return body


@pytest.fixture(scope="function")
def body_put_status_change_request_wrong_obj():
    body = {
      "id": TEST_ID_FOR_PET,
      "category": {
        "id": 423,
        "name": "string"
      },
      "name": "doggie",
      "second name": "buba",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 647,
          "name": "string"
        }
      ],
      "status": "sold"
    }
    return body


@pytest.fixture(scope="function")
def body_put_status_change_request_wrong_id():
    body = {
      "id": -45352,
      "category": {
        "id": 423,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 647,
          "name": "string"
        }
      ],
      "status": "sold"
    }
    return body
