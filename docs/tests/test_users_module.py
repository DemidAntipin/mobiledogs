from fastapi.testclient import TestClient
import random
from docs.source.main import app

client = TestClient(app)


def test_user_register():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    response = client.post("/users/register",json={"name":"testuser"+newid,"email":"testemail"+newid+"@gmail.com","phone":randphone+newid,"password":"testpassword"})
    assert response.status_code == 200
    assert response.json()["name"] == "testuser"+newid

def test_user_register_name_error():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    response = client.post("/users/register",json={"name":"test","email":"testemail"+newid+'@gmail.com',"phone":randphone+"5","password":"testpassword"})
    response = client.post("/users/register",json={"name":"test","email":"testemail2"+newid+'@gmail.com',"phone":randphone,"password":"testpassword"})
    assert response.status_code == 400
    assert response.json()["detail"] == "User with this name already registrated"

def test_user_register_email_error():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    response = client.post("/users/register",json={"name":"testuser"+newid,"email":"testemailzero@gmail.com","phone":randphone,"password":"testpassword"})
    response = client.post("/users/register",json={"name":"testuser2"+newid,"email":"testemailzero@gmail.com","phone":randphone+'52',"password":"testpassword"})
    assert response.status_code == 400
    assert response.json()["detail"] == "User with this email already registered"

def test_user_register_phone_error():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    response = client.post("/users/register",json={"name":"testuser"+newid,"email":"testemail"+newid+"@gmail.com","phone":"00000000000","password":"testpassword"})
    response = client.post("/users/register",json={"name":"testuser2"+newid,"email":"testemail2"+newid+"@gmail.com","phone":"00000000000","password":"testpassword"})
    assert response.status_code == 400
    assert response.json()["detail"] == "User with this phone already registrated"

def test_user_login():
    response = client.post("/users/login?name=testuser&password=testpassword")
    assert response.status_code == 200
    assert response.json()["name"] == "testuser"

def test_user_login_wrong_password_error():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    response = client.post("/users/register",json={"name":"testuser"+newid,"email":"testemail"+newid+"@gmail.com","phone":randphone+newid,"password":"testpassword"})
    assert response.status_code == 200
    assert response.json()["name"] == "testuser"+newid
    response = client.post("/users/login?name=testuser&password=wrongpassword")
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect name or password"

def test_get_users():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/users?token="+token)
    assert response.status_code == 200

def test_get_users_token_error():
    token="Invalid_token"
    response = client.get("/users?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_get_user():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/users/1?token="+token)
    assert response.status_code == 200

def test_get_user_token_error():
    token="Invalid_token"
    response = client.get("/users/1?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_get_user_user_not_found():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/users/-100?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "User doesn't exist"
