from cache_class import FileStrategy
import pytest
import re

class TestFile:

    @classmethod
    def setup_class(cls):
        cls.obj = FileStrategy()

    def test_getting_and_setting_data_to_database(self):
        key = 'foo1'
        data_before = self.obj.get_data(key)
        assert data_before is None

        value = 'foo1_value'
        self.obj.set_data(key, value)
        data_after = self.obj.get_data(key)
        assert data_after == value

        self.obj.delete_data()
        data_after_test = self.obj.get_data(key)
        assert data_after_test is None

    def test_strategy_method_returns_string(self):
        key = 'foo2'
        value = 'foo2_value'
        self.obj.set_data(key, value)
        returned_value = self.obj.get_data(key)
        assert isinstance(returned_value, str)
        self.obj.delete_data()

    def test_strategy_method_returns_none_value_when_nothing_was_set(self):
        key = None
        data = self.obj.get_data(key)
        assert data is None

    def test_strategy_method_does_not_take_none_value(self):
        key = 'foo3'
        value = None
        with pytest.raises(TypeError, match=re.escape('write() argument must be str, not None')):
            self.obj.set_data(key, value)

    def test_strategy_set_new_value_wih_same_key(self):
        key = 'foo3'
        value = 'first_value'
        data1 = self.obj.set_data(key, value)
        value2 = 'second_value'
        data2 = self.obj.set_data(key, value2)
        assert data1 != data2
