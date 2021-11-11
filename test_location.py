from unittest import mock
from location import find_location, validate_ip_address
from response import get_response
import pytest


def test_find_location():
    ip = '55.219.199.133'
    assert find_location(ip) == 'Sierra Vista'


def test_find_location_does_not_take_int_as_ip_address():
    ip = 1234566789
    with pytest.raises(TypeError):
        find_location(ip)


def test_find_location_does_not_take_float_as_ip_address():
    ip = 1.1
    with pytest.raises(ValueError):
        find_location(ip)


def test_validate_ip_address_with_invalid_ip_address():
    ip = 'invalid'
    with pytest.raises(ValueError):
        validate_ip_address(ip)


def test_validate_ip_address_with_valid_ip_address():
    ip = '55.219.199.133'
    assert validate_ip_address(ip) is True


@mock.patch("response.requests.get", autospec=True)
def test_get_response_successful_request(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(**{"json.return_value": {"status": "success", "city": "test_city"}})
    ip = 'test'
    assert get_response(ip) == 'test_city'
    mock_requests_get.assert_called_once()


@mock.patch("response.requests.get", autospec=True)
def test_get_response_returns_none_when_unsuccessful_request(mock_requests_get_fail):
    mock_requests_get_fail.return_value = mock.Mock(**{"json.return_value": {"status": "fail",
                                                                             "city": "second_test_city"}})
    ip = 'test2'
    assert get_response(ip) is None
    mock_requests_get_fail.assert_called_once()


def test_get_response_does_not_take_int_as_ip_address():
    ip = 1234
    with pytest.raises(TypeError):
        get_response(ip)
