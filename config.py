import pymysql
from pymysql.cursors import DictCursor
from Database import DataBase


DB_IP = "45.9.41.88"
DB_PORT = 3306
DB_USER = "Hackathon"
DB_PASSWORD = "3!eNgxu3p4cQyvvNsNV2cTSI6WJ84FWKd"
DB_NAME = "WebScanner"


def db_connect() -> DataBase: # Подключение к БД #
    try:
        db = pymysql.connect(
            host = DB_IP,
            port = DB_PORT,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME,
            cursorclass = DictCursor,
        )
    except Exception as ex:
        print("[INFO] Ошибка при работе с MySQL: ", ex)
    
    return DataBase(db, db.cursor())