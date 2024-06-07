from sqlalchemy import create_engine, text

class EmployeeTable:

    __scripts = {
        'get_employees': text("select * from employee where company_id = :company_id"),
        'select_max_id_employee': text("select max(id) from employee where company_id = :company_id"),
        'select_name_emp': text("select first_name from employee  where id = :id_emp"),
        'select_email_emp': text("select email from employee where id = :id_emp")
    }

    def __init__(self,connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self, company_id):
        return self.db.execute(self.__scripts["get_employees"], company_id=company_id).fetchall()
    def get_max_employee(self, company_id):
        return self.db.execute(self.__scripts["select_max_id_employee"], company_id=company_id).fetchone()[0]

    def  get_name_employee(self,id_emp):
        return self.db.execute(self.__scripts["select_name_emp"], id_emp=id_emp).fetchone()[0]

    def get_email_employee(self,id_emp):
        return self.db.execute(self.__scripts["select_email_emp"], id_emp=id_emp).fetchone()[0]