# import mysql.connector
from sqlalchemy.engine import create_engine
import pyodbc

server_info='DESKTOP-I8QHF1P\GOURAV'
driver='{ODBC Driver 17 for SQL Server}'
database_info='Mitel'
user_info='sa'
password_info='123'


connection_str = f'DRIVER={driver};SERVER={server_info};DATABASE={database_info};UID={user_info};PWD={password_info};TrustServerCertificate=yes'

cnxn = pyodbc.connect(connection_str)
cursor = cnxn.cursor()

#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE}'
#conn = pyodbc.connect(connectionString)
sql_query = "SELECT * from issues"
cursor.execute(sql_query)