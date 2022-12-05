import requests
import csv

from common.utils import read_config

config = read_config()
session = requests.Session() # To use one connection for all requests

### Sign up using account from MOCK_USER.csv
user_account = []

with open('MOCK_USER.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    
    for idx, row in enumerate(reader):
        if idx >= config['user_count']:
            break
        
        print (f'register account {idx+1}')
        session.post(f"{config['backend_url']}/register/", json={
            "email": row[0],
            "organization": "hospital.hospitalA",
            "organizationType": "hospital"
        })
        
        user_account.append({
            'email': row[0],
            'password': row[1],
        })
        
# register a user for insurance auditor        
session.post(f"{config['backend_url']}/register/", json={
    "email": "insuranceA@gmail.com",
    "organization": "insurance.insuranceA",
    "organizationType": "insurance"
})