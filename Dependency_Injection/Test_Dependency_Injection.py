from fastapi.testclient import TestClient
from Dependency_Injection import app, get_db_session

test_db = ["Test db"]


def get_test_db():
    return test_db


app.dependency_overrides[get_db_session] = get_test_db
Client = TestClient(app)


def test_item_should_add_to_database():
    response = Client.get("/add-item/?item=sugar")
    print(response.text)
    assert response.status_code == 200
    assert response.text == '{"message":"item added: sugar"}'
