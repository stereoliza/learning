import pytest

from cache_class import RedisStrategy


class TestRedis:

    @classmethod
    def setup_class(cls):
        cls.obj = RedisStrategy()

    def test_getting_and_setting_data_to_database(self):
        key = 'foo1'
        data_before = self.obj.get_data(key)
        assert data_before is None

        value = 'foo1_value'
        self.obj.set_data(key, value)
        data_after = self.obj.get_data(key)
        assert data_after == value

        self.obj.delete_data(key)
        data_after_test = self.obj.get_data(key)
        assert data_after_test is None

    def test_strategy_method_returns_string(self):
        key = 'foo2'
        value = 'foo2_value'
        self.obj.set_data(key, value)
        returned_value = self.obj.get_data(key)
        assert isinstance(returned_value, str)
        self.obj.delete_data(key)

    def test_strategy_method_does_not_take_none_key(self):
        key = None
        with pytest.raises(ValueError) as exception_info:
            self.obj.get_data(key)
        assert str(exception_info.value) == 'Value can not be None'

    def test_strategy_method_does_not_take_none_value(self):
        key = 'foo3'
        value = None
        with pytest.raises(ValueError, match='Value can not be None'):
            self.obj.set_data(key, value)

    def test_strategy_set_new_value_wih_same_key(self):
        key = 'foo3'
        value = 'first_value'
        data1 = self.obj.set_data(key, value)
        value2 = 'second_value'
        data2 = self.obj.set_data(key, value2)
        assert data1 != data2
