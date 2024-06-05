import requests
from time import sleep
from companyApi import CompanyApi

api = CompanyApi('https://x-clients-be.onrender.com')

def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0

def test_get_active_companies():
    body_full = api.get_company_list()
    my_params = {'active':'true'}
    body_active = api.get_company_list(params_to_add=my_params)
    assert len(body_full) > len(body_active)

def test_add_new_company():
    body = api.get_company_list()
    len_before = len(body)
    name = 'bublik'
    descr = 'no money, no honey, baby'
    res = api.create_company(name,descr)
    id_new_company = res['id']
    body_after_add = api.get_company_list()
    len_after = len(body_after_add)
    assert len_before + 1 == len_after
    assert body_after_add[-1]['name'] == name
    assert body_after_add[-1]['description'] == descr
    assert body_after_add[-1]['id'] == id_new_company

def test_get_one_company():
    name = 'Dalik'
    descr = 'no balls, no volley'
    res = api.create_company(name, descr)
    id_new_company = res['id']

    new_company = api.get_company(id_new_company)

    assert new_company['id'] == id_new_company
    assert new_company['name'] == name
    assert new_company['description'] == descr
    assert new_company['isActive'] == True

def test_edit_one_company():
    name = 'Dalik'
    descr = 'no balls, no volley'
    res = api.create_company(name, descr)
    id_new_company = res['id']

    new_name= 'updated name'
    new_descr = 'updated description'
    edted = api.edit_company(id_new_company, new_name, new_descr)
    assert edted['id'] == id_new_company
    assert edted['name'] == new_name
    assert edted['description'] == new_descr
    assert edted['isActive'] == True


def test_delete_one_company():
    name = 'Dalik'
    descr = 'no balls, no volley'
    res = api.create_company(name, descr)

    body = api.get_company_list()
    len_before = len(body)

    id_new_company = res['id']
    deleted = api.delete_company(id_new_company)
    sleep(1)
    body_after_delete = api.get_company_list()
    len_after = len(body_after_delete)
    y = body_after_delete[-1]

    assert body_after_delete[-1]['id'] != id_new_company
    assert len_before > len_after
    assert deleted['id'] == id_new_company
    assert deleted['name'] == name
    assert deleted['description'] == descr
    assert deleted['isActive'] == True
    assert body_after_delete[-1]['id'] != id_new_company

def test_deactivate_one_company():
    name = 'Dalik'
    descr = 'no balls, no volley'
    res = api.create_company(name, descr)
    new_id = res['id']
    api.deactivate_company(new_id,False)
    body_af = api.get_company_list()
    sleep(2)
    assert body_af[-1]['isActive'] == False

def test_deactivate_company_then_activate():
    name = 'Dalik'
    descr = 'no balls, no volley'
    res = api.create_company(name, descr)
    new_id = res['id']
    api.deactivate_company(new_id, False)
    body_bf = api.get_company_list()
    api.deactivate_company(new_id, True)
    body_af = api.get_company_list()
    sleep(2)
    assert body_af[-1]['isActive'] == True

def test_employe():
    name = 'Dalik'
    descr = 'no balls, no volley'
    res = api.create_company(name, descr)
    new_id = res['id']
    empl=api.get_list_employees(new_id)
    print(empl)

def test_add_employee():
    name = 'Dalik'
    descr = 'no balls, no volley'
    result = api.create_company(name, descr)
    new_id = result['id']
    res=api.add_employee(new_id,name)
    print(res)