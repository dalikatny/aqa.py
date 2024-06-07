class AddEmployeeRequest:
    def __init__(self, company_id, id=0, first_name="dalik1",
                 last_name="dalik1", middle_name="dalik1", email="dalik@dalik.ru",
                 url="string", phone="string", birthday="2024-06-05T10:41:33.877Z", is_active=True):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_mame = middle_name
        self.company_id = company_id
        self.email = email
        self.url = url
        self.phone = phone
        self.birthdate = birthday
        self.is_active = is_active

    def __iter__(self):
        yield "id", self.id
        yield "firstName", self.first_name
        yield "lastName", self.last_name
        yield "middleName", self.middle_mame
        yield "companyId", self.company_id
        yield "email", self.email
        yield "url", self.url
        yield "phone", self.phone
        yield "birthdate", self.birthdate
        yield "isActive", self.is_active
