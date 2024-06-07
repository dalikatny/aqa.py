from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

def test_db_connection():
    db = create_engine(db_connection_string)
    db.table_names()
    names = db.table_names()
    assert names[1] == 'company'

def test_db_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company  limit 10").fetchall()
    row1= rows[-1]

    assert row1['id'] == 115
    assert row1['name'] == 'hliuhlihi'

def test_select_1_row():
        db = create_engine(db_connection_string)
        sql_statement = text("select * from company where id = :comp_id")
        rows = db.execute(sql_statement, comp_id=6020).fetchall()
        assert len(rows) == 1

def test_select_2filters_row():
    db = create_engine(db_connection_string)
    sql_statement =text("select * from company where id >= :comp_id and is_active = :isActive")
    my_params = {"comp_id":6020,
                 "isActive":True}
    rows=db.execute(sql_statement, my_params).fetchall()
    assert len(rows) == 199

def test_select_3filters_row():
    db = create_engine(db_connection_string)
    sql_statement = text("insert into company (\"name\") values (:new_name)")
    rows=db.execute(sql_statement,new_name='bazazaza').fetchall()
    assert 1 == len(rows)

def test_upd_row():
    db = create_engine(db_connection_string)
    sql_statement = text("update company set description = :descr where id = :id_comp")
    rows = db.execute(sql_statement, descr='upd88dpu', id_comp=6020)

def test_delete_row():
    db = create_engine(db_connection_string)
    sql_statement = text("delete from company where id = :id_comp")
    db.execute(sql_statement, id_comp=6020)