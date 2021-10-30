from cache_class import MySQLStrategy, RedisStrategy, FileStrategy


class Strategy:

    @classmethod
    def setup_class(cls, key='foo', value='foo2'):
        cls.key = key
        cls.value = value

    def test_getting_and_setting_data_to_database(self):
        data_before = self.obj.get_data(self.key)
        assert data_before is None

        self.obj.set_data(self.key, self.value)
        data_after = self.obj.get_data(self.key)
        assert data_after == self.value

    def test_strategy_method_returns_string(self):
        returned_value = self.obj.get_data(self.key)
        assert isinstance(returned_value, str)

    @classmethod
    def teardown_class(cls):
        cls.obj.delete_data(cls.key)
        print('test data erased')


class TestMySQLStrategy(Strategy):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.obj = MySQLStrategy()


class TestRedisStrategy(Strategy):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.obj = RedisStrategy()


class TestFileStrategy(Strategy):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.obj = FileStrategy()
