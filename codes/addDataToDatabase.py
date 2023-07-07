import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancesystem-ebbed-default-rtdb.firebaseio.com/"
})



ref = db.reference('Students')

data = {
    "21cs001":
        {
            "name": "MS Dhoni",
            "major": "computer ",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "21cs002":
        {
            "name": "Elon musk",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "21cs003":
        {
            "name": "Hari narayanan ",
            "major": "Computer ",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:35"
        }
}

for key, value in data.items():
    ref.child(key).set(value)