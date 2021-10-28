from cache_class import MySQLStrategy, RedisStrategy, FileStrategy


class Strategy:
    key = 'foo'
    value = 'foo2'

    def test_getting_and_setting_data_to_database(self):
        data_before = self.obj.get_data(self.key)
        assert data_before is None

        self.obj.set_data(self.key, self.value)
        data_after = self.obj.get_data(self.key)
        assert data_after == self.value

    @classmethod
    def teardown_class(cls):
        cls.obj.delete_data(cls.key)
        print('test data erased')


class TestMySQLStrategy(Strategy):
    obj = MySQLStrategy()


class TestRedisStrategy(Strategy):
    obj = RedisStrategy()


class TestFileStrategy(Strategy):
    obj = FileStrategy()
