import requests
import csv

from common.utils import read_config

config = read_config()
session = requests.Session() # To use one connection for all requests

### Sign up using account from MOCK_USER.csv
user_account = []
user_account_insurance = []
base_url = config['backend_url'] 
print("config['isProd'] == True", config['isProd'] == True)
print("config['isProd'] == False", config['isProd'] == False)
if (config['isProd'] == True):
    base_url = config['backend_url_prod']


with open('MOCK_USER.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    
    for idx, row in enumerate(reader):
        if idx >= config['user_count']:
            break
        
        
        if idx < config['user_count'] / 2 :
            print (f'register account hospital {idx+1}')
            session.post(f"{base_url}/register/", json={
                "email": row[0],
                "organization": "hospital.hospitalA",
                "organizationType": "hospital"
            })
            user_account.append({
            'email': row[0],
            'password': row[1],
        })
        else:
            print (f'register account insurance {idx+1}')
            session.post(f"{base_url}/register/", json={
                "email": row[0],
                "organization": "insurance.insuranceA",
                "organizationType": "insurance"
            })
            user_account_insurance.append({
                'email': row[0],
                'password': row[1],
            })
        

        
# register a user for insurance auditor        
session.post(f"{base_url}/register/", json={
    "email": "ins3@gmail.com",
    "organization": "insurance.insuranceA",
    "organizationType": "insurance"
})