import string
import AddEmployeeRequest
import requests
import random
class EmployeeApi:
    creds = {
        "username": "bloom",
        "password": "fire-fairy"
    }

    def __init__(self,url):
        self.url = url


    def get_list_employees(self, id_company):
        resp = requests.get(self.url + '/employee?company=' + str(id_company))
        return resp

    def get_token(self, username="bloom", password="fire-fairy"):
        token = requests.post(self.url + '/auth/login', json=self.creds).json()['userToken']
        return token

    def add_emp(self, r: AddEmployeeRequest):
        token = self.get_token()
        return requests.post(self.url + '/employee', json=dict(r), headers={'x-client-token': token})

    def get_one_employee(self, id_emp):
        resp = requests.get(self.url + '/employee/' + str(id_emp))
        return resp

    def patch_employee(self, id_emp,):
        token = self.get_token()
        data_for_patch = {
                "lastName": "aga1rov",
                "email": "dalik11111@mail.cum",
                "url": "www.ww1w.www.google.com",
                "phone": "899991299292",
                "isActive": True
                }
        return requests.patch(self.url + '/employee/' + str(id_emp), json=data_for_patch, headers={'x-client-token': token})