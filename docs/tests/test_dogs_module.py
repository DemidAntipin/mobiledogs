from fastapi.testclient import TestClient
import random
from datetime import datetime
from docs.source.main import app

client = TestClient(app)

collarid=0
newip=""
def test_collar_register():
    newip=str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.post("/collars/register?token="+token,json={"ip":newip})
    assert response.status_code == 200
    assert response.json()["success"] == "true"

def test_collar_register_ip_error():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.post("/collars/register?token="+token,json={"ip":newip})
    response = client.post("/collars/register?token="+token,json={"ip":newip})
    assert response.status_code == 400
    assert response.json()["detail"] == "Collar with this ip already registered"

def test_collar_register_token_error():
    newip=str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))
    token="ivalid_value"
    response = client.post("/collars/register?token="+token,json={"ip":newip})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_get_collars():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/collars?token="+token)
    assert response.status_code == 200

def test_get_collars_token_error():
    token="invalid_token"
    response = client.get("/collars?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_get_collar():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/collars/1?token="+token)
    assert response.status_code == 200
    assert response.json()["id"]==1

def test_get_collar_error_token():
    token="invalid_token"
    response = client.get("/collars/1?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"]=="Invalid token"

def test_get_collar_collar_not_found():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/collars/-100?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"]=="Collar doesn't exist"


def test_dog_register():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/collars?token="+token)
    collarid=response.json()[-1]["id"]
    response = client.post("/dogs/register?token="+token,json={"name":"testname"+newid,"description":"Test description of testdog","collar_id":collarid})
    assert response.status_code == 200
    assert response.json()["success"] == "true"

def test_dog_register_token_error():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    token="invalid_token"
    response = client.post("/dogs/register?token="+token,json={"name":"testname"+newid,"description":"Test description of testdog","collar_id":collarid})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_dog_register_collar_already_used():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/collars?token="+token)
    collarid=response.json()[-1]["id"]
    response = client.post("/dogs/register?token="+token,json={"name":"testname"+newid,"description":"Test description of testdog","collar_id":collarid})
    assert response.status_code == 400
    assert response.json()["detail"] == "Dog with this collar already registered"

def test_dog_register_no_such_collar():
    newid=str(random.randint(1,10000))
    randphone=str(random.randint(10000000000,99999999999))
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.post("/dogs/register?token="+token,json={"name":"testname"+newid,"description":"Test description of testdog","collar_id":0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Collar doesn't exist"

def test_get_all_dogs():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/dogs/?token="+token)
    assert response.status_code == 200

def test_get_near_dogs():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/dogs/?token="+token+"&near=True")
    assert response.status_code == 200

def test_get_dogs_token_error():
    token="invalid_token"
    response = client.get("/dogs/?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_get_dog():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/dogs/1?token="+token)
    assert response.status_code == 200
    assert response.json()["id"]==1

def test_get_dog_token_error():
    token="invalid_token"
    response = client.get("/dogs/1?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_get_dog_not_found():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response = client.get("/dogs/0?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Dog doesn't exist"

def test_add_dogs_data():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    dogsid = client.get("/dogs/?token="+token)
    dogsid=str(dogsid.json()[-1]["id"])
    response = client.post("/dogs/"+dogsid+"/data?ip="+newip,json={"latitude":"52.290928","longitude":"104.286738","datetime":str(datetime.now())})
    assert response.status_code == 200

def test_add_dogs_data_ip_error():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    dogsid = client.get("/dogs/?token="+token)
    dogsid=str(dogsid.json()[-1]["id"])
    response = client.post("/dogs/"+dogsid+"/data?ip=wrongip",json={"latitude":"52.290928","longitude":"104.286738","datetime":str(datetime.now())})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid IP"

def test_get_dogs_status():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    dogsid = client.get("/dogs/?token="+token)
    dogsid=str(dogsid.json()[-1]["id"])
    response=client.get("/dogs/"+dogsid+"/status?token="+token)
    assert response.status_code == 200

def test_get_dogs_status_token_error():
    token="invalid_token"
    response=client.get("/dogs/"+str(1)+"/status?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

def test_get_dogs_data():
    token = client.post("/users/login?name=testuser&password=testpassword")
    token=token.json()["token"]
    response=client.get("/data?token="+token)
    assert response.status_code == 200

def test_get_dogs_data_token_error():
    token="invalid_token"
    response=client.get("/data?token="+token)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"
