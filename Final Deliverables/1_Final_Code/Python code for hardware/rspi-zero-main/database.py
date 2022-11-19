import pyrebase
import wiotp.sdk
import time
import random
d = 0

w = 0
def database(d,w,m,load,distance,lat = 10.939091,long= 78.135731):
#Initialize Firebase
  firebaseConfig={
  "apiKey": "AIzaSyB9ysbnaWc3IyeCioh-aJQT_UCMd5CBFeU",
    "authDomain": "fir-test-923b4.firebaseapp.com",
    "databaseURL": "https://fir-test-923b4-default-rtdb.firebaseio.com",
    "projectId": "fir-test-923b4",
    "storageBucket": "fir-test-923b4.appspot.com",
    "messagingSenderId": "943542145393",
    "appId": "1:943542145393:web:9b5ec7593e6a3cbd7966d0",
    "measurementId": "G-BN7JNX1Q7B"
  }
  
  firebase=pyrebase.initialize_app(firebaseConfig)
  
  db=firebase.database()
  
  # #Push Data
  data={"level":str(d)+"cm",
        "alert":m,
        "weight":str(w)+"g",
        "latitude":lat,
        "longitude":long,
        "distance_status":distance,
        "load_status":load}
  # print(db.push(data)) 
  
  
  # update data base
  
  db.child("-NEkRRkKsX7yVcqy_rK4").update(data)

  myConfig = {
      "identity": {
          "orgId": "4yi0vc",
          "typeId": "smartwaste123",
          "deviceId":"70103"
      },
      "auth": {
          "token": "123456789"
      }
  }
  
  def myCommandCallback(cmd):
      print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
      m=cmd.data['command']
  
  client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
  client.connect()
  client.publishEvent(eventId="status", msgFormat="json", data=data, qos=0, onPublish=None)




