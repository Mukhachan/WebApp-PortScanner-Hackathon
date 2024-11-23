from datetime import datetime
from pymysql import  Connection 
from pymysql.cursors import DictCursor
from dateutil import tz

timezon = tz.gettz('Europe/Moscow')

class DataBase:
    def __init__(self, connection = None, cursor = None): # Инициализация глобальных переменных # 
        self.__connection: Connection[DictCursor]  = connection
        self.__cur: DictCursor = cursor