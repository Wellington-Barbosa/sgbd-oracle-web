import os
import cx_Oracle

# Parâmetros de conexão com o Oracle

DB_USERNAME = 'tasy'
DB_PASSWORD = 'aloisk'
DB_HOST = '172.24.1.191'
DB_PORT = '1521'
DB_SERVICE = 'DBTST'
DB_INSTANCE = 'DBTST'

def get_db_connection():
    dsn = cx_Oracle.makedsn(DB_HOST, DB_PORT, service_name=DB_SERVICE)
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, dsn)
    return connection