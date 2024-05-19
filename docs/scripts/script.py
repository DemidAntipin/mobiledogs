import collar
import time
import requests
import random
from multiprocessing import Process

def regdog(token,collar_ip,dogs_name):
   dogs_desc="A furry Haski"
   collarreg=requests.post(url+"/collars/register?token="+token,json={"ip":collar_ip})
   if (collarreg.status_code==400):
      collarget=requests.get(url+"/collars/getbyip/"+collar1_ip+"/?token="+token)
      collar_id=collarget.json()["id"]
   elif (collarreg.status_code==200):
      collar_id=collarreg.json()["id"]
   dogreg=requests.post(url+"/dogs/register/?token="+token,json={"name": dogs_name,"description": dogs_desc,"collar_id":collar_id})
   if(dogreg.status_code==400):
      dogs=requests.get(url+"/dogs/?token="+token)
      for i in range(len(dogs.json())):
          if (dogs.json()[i]["name"]==dogs_name):
             dogid=dogs.json()[i]["id"]
             break
   elif (dogreg.status_code==200):
      dogid=dogreg.json()["dog_id"]
   return dogid


print("Input url (http://domen):")
url=input()
name="admin"
password="admin"
token=""
collar_id=""
login=requests.post(url+"/users/login/?name="+name+"&password="+password)
if (login.status_code==400):
    login=requests.post(url+"/users/register/",json={"name": name,"email": name+"@gmail.com","phone": str(random.randint(10000000000,99999999999)),"password": password})
token=login.json()["token"]

collar1_ip=str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))+"."+str(random.randint(1000,9999))
dogs_name1="Bobyk"+str(random.randint(100,9999))
dogid1=regdog(token,collar1_ip,dogs_name1)

if __name__ == '__main__':
    collar.start_send_requests(url,collar1_ip,dogid1)
