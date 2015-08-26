import pymssql
from project.local_settings import db_server_rj, db_user_rj, db_password_rj, db_database_rj
from project.local_settings import db_server_sp, db_user_sp, db_password_sp, db_database_sp


def exec_sql(sql, filial):
    """ executa o sql """
    if filial == 'SAO':
        conn = pymssql.connect(db_server_sp, db_user_sp, db_password_sp, db_database_sp)
    else: 
        conn = pymssql.connect(db_server_rj, db_user_rj, db_password_rj, db_database_rj)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchone()
    conn.close()
    return rows

def get_hotel_code(hotel_name, filial):
    sql = "select codfor from e095for where apefor = '%s'" % hotel_name
    sqlcmnet = "select codfor from e095for where USU_CMNET = '%s'" % hotel_name
    sqlehtl = "select codfor from e095for where USU_EHTL = '%s'" % hotel_name
    sqltrend = "select codfor from e095for where USU_TREND = '%s'" % hotel_name
    sqlhtldo = "select codfor from e095for where USU_HTLDO = '%s'" % hotel_name
    rows = exec_sql(sql, filial)
    if rows:
    	return rows[0]
    rows = exec_sql(sqlcmnet, filial)
    if rows:
        return rows[0]
    rows = exec_sql(sqlehtl, filial)
    if rows:
        return rows[0]
    rows = exec_sql(sqltrend, filial)
    if rows:
        return rows[0]
    rows = exec_sql(sqlhtldo, filial)
    if rows:
        return rows[0]
    #nao achou
    return 0

def get_regente_code(bkagt, filial):
    sql = "Select UsuIea from V099UTU where UsuAma = '%s'" % bkagt
    rows = exec_sql(sql, filial)
    if rows:
    	return rows[0].split('/')[1]
    else:
        return 0
