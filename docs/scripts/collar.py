import requests
import random
from datetime import datetime
import time
def start_send_requests(url,ip,dog_id):
    latitude=random.random()*100
    longitude=random.random()*100
    while(True):
        response=requests.post(url+"/dogs/"+str(dog_id)+"/data?ip="+ip,json={"latitude":str(latitude),"longitude":str(longitude),"datetime":str(datetime.now())})
        latitude+=(random.random()/10)
        longitude+=(random.random()/10)
        time.sleep(60)
