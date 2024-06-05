import requests

base_url='https://x-clients-be.onrender.com'
id_company = 5989
employee_data = {
            "id": 0,
            "firstName": "dalik1",
            "lastName": "dalik1",
            "middleName": "dalik1",
            "companyId": id_company,
            "email": "dalik@dalik.ru",
            "url": "string",
            "phone": "string",
            "birthdate": "2024-06-05T10:41:33.877Z",
            "isActive": True
        }
creds = {
        "username": "bloom",
        "password": "fire-fairy"
    }
def test_get_employees():
    resp = requests.get(base_url+'/employee?company='+str(id_company))
    assert resp.status_code == 200
    assert resp.json()

def test_auth():
    creds={
        "username": "bloom",
        "password": "fire-fairy"
    }
    resp = requests.post(base_url+'/auth/login', json=creds)
    assert resp.status_code == 201
    token = resp.json()['userToken']
    return token
def test_add_employee():
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()['userToken']

    resp = requests.post(base_url + '/employee', json=employee_data , headers={'x-client-token': token})
    assert resp.status_code == 201
    id_emp = resp.json()['id']
    return id_emp

id_emp = test_add_employee()
def test_get_employee():
    resp = requests.get(base_url+'/employee/'+str(id_emp))
    assert resp.status_code == 200
    assert resp.json()['firstName'] == employee_data['firstName']

def test_patch_employee():
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()['userToken']
    data_for_patch= {
        "lastName": "aga1rov",
        "email": "dalik11@mail.cum",
        "url": "www.ww1w.www.google.com",
        "phone": "899991299292",
        "isActive": True
    }
    resp = requests.patch(base_url + '/employee/'+str(id_emp),headers={'x-client-token': token}, json=data_for_patch)
    assert resp.status_code == 201