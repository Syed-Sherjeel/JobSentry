import json


def test_create_user(client):
    data = {
        "username": "test_user",
        "email": "testuser@nofoobar.com",
        "password": "testing",
    }
    response = client.post("/users/create-user", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] is True
