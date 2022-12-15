from locust import HttpUser, task
import random
import csv

from common.utils import read_config

config = read_config()

class EHRSystemLoadTest(HttpUser):
    
    user_account = {}
    user_account_insurance = {}
    list_ehr_id = [
        '03c3223f-eefc-4ce1-8d53-7151dbf77fb5',
        '0fc6d967-ac3f-4982-8339-e10fa299f8cc',
        '2a526356-1494-4c7c-847f-5fc412e9d852',
        '37aecb95-c8df-463d-91ab-3fe8f0a3fb71',
        'ca0d1ce4-31b9-483f-86ca-849fac7538b3',
        'dc6cda80-8626-4fa9-881d-80385a649995',
        'e3b516c0-f1ff-4054-b7da-5eda622d7043',
        'e92617f7-7ed7-43d9-881e-6413530ed837',
        'f7724a8f-d5de-49c5-b051-b4bce88e00f6',
        'fa4a7dd2-430b-40bd-9191-5fe62ab0eef9'
    ]
    header = {}
    header_insurance = {}
    error_log_id = None

    # @task
    # def login(self):
    #     self.client.post("/login/", json={
    #         'email': self.user_account['email'],
    #         'password': self.user_account['password'],
    #     })

    @task
    def create_ehr(self):
        response = self.client.post(f"/ehr/", json={
                "name": "budi",
                "dateOfBirth": "1990-11-29T21:02",
                "address": "Jalan Kemanggisan Raya no. 1, Jakarta Barat",
                "phoneNumber": "0851111112223",
                "gender": "male", 
                "nationality": "Indonesia",
                "bloodType": "A+",
                "height": "170",
                "weight": "70",
                "pulseRate": "60",
                "bloodPressure": "140/90",
                "respiratoryRate": "20",
                "medicalHistory": [
                    {
                        "date": "2022-11-29T21:02",
                        "description": "medical check-up 1"
                    },
                    {
                        "date": "2022-11-29T21:02",
                        "description": "medical check-up 2"
                    }
                ],
                "diagnose": [
                    {
                        "date": "2022-11-29T21:02",
                        "description": "diagnose 1"
                    },
                    {
                        "date": "2022-11-29T21:02",
                        "description": "diagnose 2"
                    }
                ],
                "insuranceName": "insuranceA"
                
            }, headers=self.header)
        # ehr = response.json()
        # if (ehr.get('ehrId', None) != None):
        #     self.list_ehr_id.append(ehr['ehrId'])
    

    @task
    def update_ehr(self):
        ehr_id = random.choice(self.list_ehr_id)
        self.client.put(f"/ehr/{ehr_id}", json={
                "name": "newname",
                "dateOfBirth": "1990-11-29T21:02",
                "address": "Jalan Kemanggisan Raya no. 1, Jakarta Barat",
                "phoneNumber": "0851111112223",
                "gender": "male", 
                "nationality": "Indonesia",
                "bloodType": "A+",
                "height": "170",
                "weight": "70",
                "pulseRate": "60",
                "bloodPressure": "140/90",
                "respiratoryRate": "20",
                "medicalHistory": [
                    {
                        "date": "2022-11-29T21:02",
                        "description": "medical check-up 1"
                    },
                    {
                        "date": "2022-11-29T21:02",
                        "description": "medical check-up 2"
                    },
                    {
                        "date": "2022-11-29T21:02",
                        "description": "medical check-up 3"
                    }
                ],
                "diagnose": [
                    {
                        "date": "2022-11-29T21:02",
                        "description": "diagnose 1"
                    },
                    {
                        "date": "2022-11-29T21:02",
                        "description": "diagnose 2"
                    },
                    {
                        "date": "2022-11-29T21:02",
                        "description": "diagnose 3"
                    }
                ],
                "insuranceName": "insuranceA"
                
        }, headers=self.header)
    
    @task
    def get_detail_ehr(self):
        ehr_id = random.choice(self.list_ehr_id)
        self.client.get(f"/ehr/{ehr_id}", headers=self.header)
    
    @task
    def get_history_ehr(self):
        ehr_id = random.choice(self.list_ehr_id)
        self.client.get(f"/ehr/history/{ehr_id}", headers=self.header)
    
    @task
    def get_all_ehr(self):
        self.client.get("/ehr/", headers=self.header)
    
    @task
    def get_insured_ehr(self):
        self.client.get("/insurance/ehr/", headers={'Authorization': "ins3@gmail.com"})
        # self.client.get("/insurance/ehr/", headers=self.header_insurance)
        
    def on_start(self):
        # Read user mock
        with open('MOCK_USER.csv', newline='') as csv_file:
            reader = csv.reader(csv_file)
            users = []
            users_insurance = []
            
            for idx, row in enumerate(reader):
                if idx >= config['user_count']:
                    break
            
                if idx < config['user_count'] / 2 :
                    users.append({
                    'email': row[0],
                    'password': row[1],
                    })
                    self.user_account = random.choice(users)
                    
                    # Login to account
                    response = self.client.post("/login/", json={
                        'email': self.user_account['email'],
                        'password': self.user_account['password'],
                    })
                    self.header = {'Authorization': f"{self.user_account['email']}"}

                else:
                    users_insurance.append({
                        'email': row[0],
                        'password': row[1],
                    })
                    self.user_account_insurance = random.choice(users_insurance)

                    response = self.client.post("/login/", json={
                        'email': self.user_account_insurance['email'],
                        'password': self.user_account_insurance['password'],
                    })                    
                    self.header_insurance = {'Authorization': f"{self.user_account_insurance['email']}"}
                
            for i in range(5):
                response = self.client.post(f"/ehr/", json={
                    "name": f"budi{i}",
                    "dateOfBirth": "1990-11-29T21:02",
                    "address": "Jalan Kemanggisan Raya no. 1, Jakarta Barat",
                    "phoneNumber": "0851111112223",
                    "gender": "male", 
                    "nationality": "Indonesia",
                    "bloodType": "A+",
                    "height": "170",
                    "weight": "70",
                    "pulseRate": "60",
                    "bloodPressure": "140/90",
                    "respiratoryRate": "20",
                    "medicalHistory": [
                        {
                            "date": "2022-11-29T21:02",
                            "description": "medical check-up 1"
                        },
                        {
                            "date": "2022-11-29T21:02",
                            "description": "medical check-up 2"
                        }
                    ],
                    "diagnose": [
                        {
                            "date": "2022-11-29T21:02",
                            "description": "diagnose 1"
                        },
                        {
                            "date": "2022-11-29T21:02",
                            "description": "diagnose 2"
                        }
                    ],
                    "insuranceName": "insuranceA"
                    
                }, headers=self.header)
                # ehr = response.json()
                # if (ehr.get('ehrId', None) != None):
                #     self.list_ehr_id.append(ehr['ehrId'])
        print('self.header ', self.header)
        print('self.header_insurance ', self.header_insurance)
        
        

    # tasks = [get_all_ehr]    
            
        
        
        