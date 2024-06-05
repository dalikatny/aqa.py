import json

company_json = """
        {
            "id" : 111,
            "IsSctive" : true,
            "createDateTime" : "2022-05-27",
            "lastChangeDateTime" : "2022-05-27",
            "name" : "Abrbershop",
            "description" : "Nice haircut"
        }       
    """

company_list_json= """
[    
    {
        "id" : 111,
            "IsSctive" : true,
            "createDateTime" : "2022-05-27",
            "lastChangeDateTime" : "2022-05-27",
            "name" : "Abrbershop",
            "description" : "Nice haircut"
    },
    {
            "id" : 112,
            "IsSctive" : false,
            "createDateTime" : "2012-05-27",
            "lastChangeDateTime" : "2012-05-27",
            "name" : "Abrber1shop",
            "description" : "Nicqe haircut"
            }
]
"""
def test_parse_json():
    company = json.loads(company_json)
    assert  company["id"] == 111

def test_parse_array_json():
    company_list = json.loads(company_list_json)
    first_company = company_list[0]
    assert first_company["name"] == "Abrbershop"

    assert company_list[1][id] == 112
