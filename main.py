import pyrebase
import time

firebaseConfig = {
    "apiKey": "AIzaSyAYIhWRLfqHSdHIpG8DN3OXUoZ6uo8csHY",
    "authDomain": "breakingstuff-300b4.firebaseapp.com",
    "databaseURL": "https://breakingstuff-300b4-default-rtdb.firebaseio.com",
    "projectId": "breakingstuff-300b4",
    "storageBucket": "breakingstuff-300b4.appspot.com",
    "messagingSenderId": "1060088119663",
    "appId": "1:1060088119663:web:faa4385be68547fb35e89a",
    "measurementId": "G-YCZPDR6HZX"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
t0 = 0
t1 = 0
time_elapsed = 0
while True:
    t0 = time.time()
    x_val = db.child("X").get().val()
    y_val = db.child("Y").get().val()
    z_val = db.child("Z").get().val()
    t1 = time.time()

    time_elapsed = t1 - t0

    print(time_elapsed)
    print()
    print("X :", x_val)
    print("Y :", y_val)
    print("Z :", z_val)
    print()





