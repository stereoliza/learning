from cache_class import MySQLStrategy, RedisStrategy, FileStrategy


class CacheService:

    def __init__(self):
        self.strategy = None

    @staticmethod
    def pick_strategy():
        try:
            obj = MySQLStrategy()
            check = obj.is_available()
            if check is True:
                return MySQLStrategy()
        except:
            print('MySQL is not available')

        try:
            obj = RedisStrategy()
            check = obj.is_available()
            if check is True:
                return RedisStrategy()
        except:
            print('Redis is not available')

        try:
            obj = FileStrategy()
            check = obj.is_available()
            if check is True:
                return FileStrategy()
        except:
            print('No cache available')

    def get_value(self, key):
        value = self.__get_strategy().get_data(key)
        return value

    def set_value(self, key, value):
        self.__get_strategy().set_data(key, value)
        print(value)
        return value

    def __get_strategy(self):
        if not self.strategy:
            self.strategy = self.pick_strategy()
        return self.strategy
