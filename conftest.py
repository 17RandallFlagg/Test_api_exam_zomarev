import pytest


@pytest.fixture(scope="function")
def body_post_request():
    body = {
      "id": 578,
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
      "id": 578,
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
      "id": 578,
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
      "id": 5786700000000000000000000000000000000045,
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
def body_put_status_change_request_wrong_id():
    body = {
      "id": "5wq8",
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
