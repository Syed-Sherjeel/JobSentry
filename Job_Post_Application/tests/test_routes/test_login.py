import json


def test_successful_login(client):
    data = {
        "username": "doradominic",
        "password": "asfdas1",
        "email": "user11@example.com",
    }
    _ = client.post("/users/create-user/", content=json.dumps(data))
    data = {"username": "user11@example.com", "password": "asfdas1"}
    response = client.post("/login/token", data=data)
    assert response.status_code == 200


def test_failed_login(client):
    data = {
        "username": "doradominic",
        "password": "asfdas1",
        "email": "user11@example.com",
    }
    _ = client.post("/users/create-user", content=json.dumps(data))
    data = {"username": "fakeuser@example.com", "password": "asfdas1"}
    response = client.post("/login/token", data=data)
    assert response.status_code == 401
