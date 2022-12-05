from locust import HttpUser, task
import random
import csv

from common.utils import read_config

config = read_config()

class EHRSystemLoadTest(HttpUser):
    user_account = {}
    list_ehr_id = []
    header = {}
    error_log_id = None
    
    # @task
    # def createNewTeam(self):
    #     self.client.post("/team-management/", json={
    #         'name': "team-name",
    #         'description': "team-description",
    #         'logo': None,
    #     }, headers=self.header)

    # @task
    # def editTeam(self):
    #     resp = self.client.get("/auth/current_team/", headers=self.header)
    #     resp_current_team = resp.json()
        
    #     self.client.put(f"/team-management/{resp_current_team['id']}/", json={
    #         'description': "team-description",
    #         'logo': None,
    #     }, headers=self.header)        

    # @task
    # def createEhr(self):
    #     resp = self.client.get("/auth/current_team/", headers=self.header)
    #     resp_current_team = resp.json()
        
    #     self.client.put(f"/team-management/{resp_current_team['id']}/", json={
    #         'description': "team-description",
    #         'logo': None,
    #     }, headers=self.header)  

    @task
    def login(self):
        self.client.post("/login/", json={
            'email': self.user_account['email'],
            'password': self.user_account['password'],
        })


    @task
    def create_ehr(self):
        self.client.post(f"/ehr/", json={
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
        self.client.get("/insurance/ehr/", headers={'Authorization': "insuranceA@gmail.com"})
        
    def on_start(self):
        # Read user mock
        with open('MOCK_USER.csv', newline='') as csv_file:
            reader = csv.reader(csv_file)
            users = []
            
            for idx, row in enumerate(reader):
                if idx >= config['user_count']:
                    break
                
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
        
        # access_token = response.json()['token']
        self.header = {'Authorization': f"{self.user_account['email']}"}
        
        # Standard Create EHR
        for i in range(5):
            resp = self.client.post(f"/ehr/", json={
                "name": "mii",
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
            ehr = resp.json()
            self.list_ehr_id.append(ehr['ehrId'])
            
        
        
        