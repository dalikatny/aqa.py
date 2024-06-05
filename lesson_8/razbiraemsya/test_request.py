import requests

base_url='https://x-clients-be.onrender.com'
def test_request():

    resp = requests.get(base_url+'/company')
    responce_body = resp.json()
    first_company = responce_body[0]
    assert resp.status_code == 200
    assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert first_company['name'] == "Барбершоп 'ЦирюльникЪ'"

def test_auth():
    creds={
        "username": "bloom",
        "password": "fire-fairy"
    }
    resp = requests.post(base_url+'/auth/login', json=creds)
    assert resp.status_code == 201
    token = resp.json()['userToken']
    return token

def test_create():
    creds={
        "username": "bloom",
        "password": "fire-fairy"
    }
    company={
        "name": "Dalik",
        "descrption": "ububububu"
    }

    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()['userToken']

    create=requests.post(base_url + '/company', json=company, headers={'x-client-token': token})
    assert create.status_code == 201