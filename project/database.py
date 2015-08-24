import pymssql
from project.local_settings import db_server, db_user, db_password, db_database

def exec_sql(sql):
	""" executa o sql """
	conn = pymssql.connect(db_server, db_user, db_password, db_database)
	cursor = conn.cursor()
	cursor.execute(sql)
	rows = cursor.fetchone()
	conn.close()
	return rows

def get_hotel_code(hotel_name):
    sql = "select codfor from e095for where apefor = '%s'" % hotel_name
    rows = exec_sql(sql)
    if rows:
    	return rows[0][0]

def get_regente_code(bkagt):
    sql = "Select UsuIea V099UTU where UsuAma = '%s'" % bkagt
    rows = exec_sql(sql)
    if rows:
    	return rows[0][0]
