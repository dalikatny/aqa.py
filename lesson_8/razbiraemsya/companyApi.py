import string

import requests
import random
class CompanyApi:
    def __init__(self,url):
        self.url = url

    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        body = resp.json()
        return body

    def get_token(self, username="bloom", password="fire-fairy"):
        creds = {
            "username": username,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        token = resp.json()['userToken']
        return token

    def create_company(self, name, description=''):
        token = self.get_token()
        company = {
            "name": name,
            "description": description
        }
        create = requests.post(self.url + '/company', json=company, headers={'x-client-token': token})
        return create.json()
    def get_company(self, company_id):
        resp = requests.get(self.url + '/company/' + str(company_id))
        return resp.json()

    def create_random_company(self):
        token = self.get_token()
        company = {
            "name": [random.choice(string.ascii_uppercase + string.digits) for _ in range(10)],
            "description": [random.choice(string.ascii_uppercase + string.digits) for _ in range(10)]
        }
        create = requests.post(self.url + '/company', json=company, headers={'x-client-token': token})
        return create.json()
    def edit_company(self, company_id, name, description):
        token = self.get_token()
        company = {
            "name": name,
            "description": description
        }
        resp=requests.patch(self.url + '/company/' + str(company_id), headers={'x-client-token': token},json=company)
        return resp.json()
    def delete_company(self, company_id):
        token = self.get_token()
        resp=requests.get(self.url + '/company/delete/' + str(company_id), headers={'x-client-token': token})
        return resp.json()
    def deactivate_company(self, company_id, isActive):
        token = self.get_token()
        resp = requests.patch(self.url + '/company/status/' + str(company_id), headers={'x-client-token': token}, json={'isActive': isActive})
        return resp.json()

    def get_list_employees(self, company_id):
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()

    def add_employee(self, company_id, name, lastname=None,middleName=None,email=None,url=None,phone=None,birthday="2024-05-17T15:31:03.048Z"):
        token = self.get_token()
        empl={
            "id": 0,
            "firstName": name,
            "lastName": lastname,
            "middleName": middleName,
            'companyId' : company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthday
             }
        resp = requests.post(self.url + '/employee', headers={'x-client-token': token},json=empl)
        return resp.json()