from sqlalchemy import create_engine, text

class CompanyTable:
    __scripts = {
        'select': "select * from company",
        'select_active': "select * from company where is_active=TRUE",
        'delete':  text("delete from company where id = :id_to_delete"),
        'insert new': text("insert into company(name, description) values (:new_name, :new_description)"),
        'get_id_max': text("select MAX(id) from company"),
        'get_employees': text("select * from employee where company_id = :company_id")
    }

    def __init__(self,connection_string):
        self.db = create_engine(connection_string)

    def get_company(self):
       return self.db.execute(self.__scripts['select']).fetchall()

    def get_active_company(self):
        return self.db.execute(self.__scripts['select_active']).fetchall()

    def delete_company(self,id):
        return self.db.execute(self.__scripts['delete'],id_to_delete=id)

    def create(self, name, description):
        return self.db.execute(self.__scripts['insert new'],new_name=name,new_description=description)

    def get_max_id (self):
        return self.db.execute(self.__scripts["get_id_max"]).fetchall()[0][0]
