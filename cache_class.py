from abc import ABC, abstractmethod
import mysql.connector as mysql
from mysql.connector import errorcode
import redis


class CacheStrategy(ABC):

    def __init__(self):
        self.connection = None

    @abstractmethod
    def get_data(self, key):
        pass

    @abstractmethod
    def set_data(self, key, value):
        pass

    @abstractmethod
    def is_available(self):
        pass


class MySQLStrategy(CacheStrategy):

    def __init__(self, host='localhost', user='root', password='pass', dbname='learningdb'):
        super().__init__()
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.cursor = self.__get_connection().cursor()

    def __get_connection(self):
        """
        Connect to database
        :return:
        """
        if not self.connection:
            self.connection = mysql.connect(host=self.host,
                                            user=self.user,
                                            password=self.password,
                                            database=self.dbname)
            return self.connection
        else:
            return self.connection

    def is_available(self) -> bool:
        """
        Check if strategy is available
        :return:bool
        """
        connection = self.__get_connection()
        if connection:
            return True
        return False

    def __create_table(self):
        TABLES = {}
        TABLES['key_value'] = (
            "CREATE TABLE IF NOT EXISTS `key_value` ("
            "  `key` varchar(25),"
            "  `value` varchar(255),"
            "  PRIMARY KEY (`key`)"
            ") ENGINE=InnoDB")
        try:
            table_description = TABLES['key_value']
            self.__get_connection().cursor().execute(table_description)
        except mysql.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                pass

    def __check_if_table_exists(self):
        show_table = "SHOW TABLES LIKE 'key_value'"
        self.cursor.execute(show_table)
        result = self.cursor.fetchone()
        if result:
            pass
        else:
            self.__create_table()

    def get_data(self, key: str) -> str:
        """
        return value from cache
        :param key: str
        :return: str
        """
        self.__check_if_table_exists()
        get_value = "SELECT `value` FROM key_value WHERE `key` = %s"
        key_v = (key,)
        self.cursor.execute(get_value, key_v)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def set_data(self, key, value):
        """
        set value to cache
        :param key: str
        :param value: str
        :return: str
        """
        insert = "INSERT INTO key_value (`key`, `value`) VALUES (%s,%s)"
        insert_values = (key, value)
        self.cursor.execute(insert, insert_values)
        self.connection.commit()

    def delete_data(self, key):
        """
        delete data from database
        :param key:
        :return:
        """
        delete = "DELETE FROM `key_value` WHERE `key` = %s"
        key_v = (key, )
        self.cursor.execute(delete, key_v)
        self.connection.commit()


class RedisStrategy(CacheStrategy):

    def __init__(self, host='localhost', port=6379, db=0, decode_responses=True):
        super().__init__()
        self.host = host
        self.port = port
        self.db = db
        self.decode = decode_responses
        self.redis_client = self.__get_connection()

    def __get_connection(self):
        if self.connection is None:
            self.connection = redis.Redis(host=self.host,
                                          port=self.port,
                                          db=self.db,
                                          decode_responses=self.decode)
            return self.connection
        return self.connection

    def is_available(self) -> bool:
        """
        Check if strategy is available
        :return:
        """
        connection = self.__get_connection
        if connection:
            return True
        return False

    def get_data(self, key):
        result = self.redis_client.get(key)
        if result:
            return result
        return None

    def set_data(self, key, value):
        self.redis_client.set(key, value)
        print(value)
        return value

    def delete_data(self, key):
        self.redis_client.delete(key)


class FileStrategy(CacheStrategy):

    def __init__(self, filename='cache.txt'):
        super().__init__()
        self.name = filename
        self.file = self.__get_connection()

    def __get_connection(self):
        if not self.connection:
            self.connection = open(self.name, "w")
        return self.connection

    def is_available(self) -> bool:
        """
        Check if strategy is available
        :return:
        """
        connection = self.__get_connection()
        if connection:
            return True
        return False

    def get_data(self, key):
        response = open(self.name, "r").read()
        if response == '':
            return None
        else:
            return response

    def set_data(self, key, value):
        open(self.name, "w").write(value)
        open(self.name, "r").close()
        return value

    def delete_data(self, key):
        self.file.close()
