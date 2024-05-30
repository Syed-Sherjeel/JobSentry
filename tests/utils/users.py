from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from schema.users import CreateUser
from db.repository.users import get_user_by_email
from db.repository.users import create_new_user


def authenticate_token_from_email(client: TestClient, db: Session):
    email = "testuser@aol.com"
    password = "q123fa*124!_+!@"
    user = get_user_by_email(email, db)
    if not user:
        user = CreateUser(username=email, email=email, password=password)
        create_new_user(user, db)
    return user_authentication_header(client, email, password)


def user_authentication_header(client: TestClient, email: str, password: str):
    data = {"username": email, "password": password}
    response = client.post("/login/token", data=data)
    auth_token = response.json()["access_token"]
    return {"Authorization": f"Bearer {auth_token}"}
