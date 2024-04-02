import requests
import json


URL = 'http://127.0.0.1:8000/create/'

data = {
    'students_name' : 'Hamidur Rahman',
    'student_subject' : 'Math',
    'student_age' : 23
}


#convert python data to json

json_data = json.dumps(data)

r = requests.post(url=URL, data= json_data)

data = r.json()

print(data)