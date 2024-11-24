from datetime import datetime
from pymysql import  Connection 
from pymysql.cursors import DictCursor
import time
from dateutil import tz

timezon = tz.gettz('Europe/Moscow')

class DataBase:
    def __init__(self, connection = None, cursor = None): # Инициализация глобальных переменных # 
        self.__connection: Connection[DictCursor]  = connection
        self.__cur: DictCursor = cursor

    def insert_ip(self, data) -> bool:
        ip = data['ip']
        port = data['port']

        # Создаем строку запроса для проверки наличия записи по IP и порту
        sql_check_exists = """
            SELECT id 
            FROM results 
            WHERE ip = %s AND port = %s"""
        
        try:
            db = self.__cur
            db.execute(sql_check_exists, (ip, port))
            existing_id = db.fetchone()

            if existing_id is not None:  # Если запись существует, обновляем ее
                pass
            else:  # Если запись не существует, создаем новую
                sql_insert = """
                    INSERT INTO results (search_id, ip, port, country, city, service, message, datetime) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """

                val = (data['search_id'], data['ip'], data['port'], data['country'], data['city'], data['service'], data['message'], data['datetime'])
                db.execute(sql_insert, val)

            self.__connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def is_ip_in_db(self, ip, port) -> bool:
        # Создаем строку запроса для проверки наличия записи по IP и порту
        sql_check_exists = """
            SELECT id 
            FROM results
            WHERE ip = %s AND port = %s"""
        try:
            db = self.__cur
            db.execute(sql_check_exists, (ip, port))
            existing_id = db.fetchone()
            if existing_id is not None:
                return True
            else:
                return False
        except Exception as ex:
            print(f"Error {ex}")
            return False
    
    def every_ip_to_check(self, ip) -> bool:
        sql_check_exists = """
            SELECT datetime 
            FROM results
            WHERE ip = %s"""
        try:
            db = self.__cur
            db.execute(sql_check_exists, (ip))
            datetime_for_check = db.fetchone()
            return datetime_for_check
        except Exception as ex:
            print(f"Error {ex}")
            return False
        

    def give_me_all(self):
        #Просто функция чтобы получить всё из базы данных
        db = self.__cur
        db.execute("SELECT * FROM results")
        
        return db.fetchall()

    def fetch_result(self, ip):
        pass
        #return None