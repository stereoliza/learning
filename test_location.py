from unittest import mock
from location import find_location, validate_ip_address
from response import get_response
import pytest


def test_find_location():
    ip = '55.219.199.133'
    print(ip)
    assert find_location(ip) == 'Sierra Vista'


def test_validate_ip_address_with_invalid_ip_address():
    ip = 'invalid'
    with pytest.raises(ValueError):
        validate_ip_address(ip)


def test_validate_ip_address_with_valid_ip_address():
    ip = '55.219.199.133'
    assert validate_ip_address(ip) is True


@mock.patch("response.requests.get", autospec=True)
def test_get_response(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(**{"json.return_value": {"status": "success", "city": "test_city"}})
    ip = 'test'
    assert get_response(ip) == 'test_city'
    mock_requests_get.assert_called_once()




