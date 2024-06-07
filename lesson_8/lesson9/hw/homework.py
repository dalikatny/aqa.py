import requests
from EmployeeTable import EmployeeTable
from EmployeeApi import EmployeeApi
from AddEmployeeRequest import AddEmployeeRequest
api = EmployeeApi('https://x-clients-be.onrender.com')
db = EmployeeTable('postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx')

base_url='https://x-clients-be.onrender.com'
id_company = 6456
creds = {
        "username": "bloom",
        "password": "fire-fairy"
    }
def test_get_employees():
    resp_api=api.get_list_employees(id_company).json()
    sk_api=api.get_list_employees(id_company).status_code
    resp_db=db.get_employees(id_company)
    assert sk_api == 200
    assert len(resp_db)==len(resp_api)

def test_add_employee():
    r = AddEmployeeRequest(company_id=id_company)
    resp_api=api.add_emp(r)
    resp_db = db.get_max_employee(id_company)
    assert resp_api.status_code==201
    assert resp_api.json()['id']==resp_db


def test_get_employee():
    r = AddEmployeeRequest(company_id=id_company,)
    resp_api = api.add_emp(r)
    new_id = resp_api.json()['id']
    new_emp = api.get_one_employee(new_id).json()['firstName']
    name_emp = db.get_name_employee(new_id)
    id_new_emp = db.get_max_employee(id_company)
    assert new_id == id_new_emp
    assert new_emp == name_emp
    assert resp_api.status_code == 201

def test_patch_employee():
    r = AddEmployeeRequest(company_id=id_company, )
    resp_api = api.add_emp(r)
    new_id = resp_api.json()['id']
    emp_api=api.patch_employee(new_id)
    email_emp_api=emp_api.json()['email']
    email_emp_db = db.get_email_employee(new_id)
    assert email_emp_db == email_emp_api


