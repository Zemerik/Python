"""
Exercise 2: API Client Test Coverage
Build test coverage for an API client:
- Mock HTTP responses
- Test error handling
- Validate JSON parsing
(Use unittest and unittest.mock.)
"""

import unittest
from unittest.mock import patch, Mock
import requests

# Simulated API client
class APIClient:
    def fetch_data(self, url):
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()

class TestAPIClient(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        mock_resp = Mock()
        mock_resp.raise_for_status = Mock()
        mock_resp.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_resp
        client = APIClient()
        data = client.fetch_data('http://example.com')
        self.assertEqual(data, {'key': 'value'})
    @patch('requests.get')
    def test_fetch_data_http_error(self, mock_get):
        mock_resp = Mock()
        mock_resp.raise_for_status.side_effect = requests.HTTPError('error')
        mock_get.return_value = mock_resp
        client = APIClient()
        with self.assertRaises(requests.HTTPError):
            client.fetch_data('http://example.com')
    @patch('requests.get')
    def test_fetch_data_json_error(self, mock_get):
        mock_resp = Mock()
        mock_resp.raise_for_status = Mock()
        mock_resp.json.side_effect = ValueError('bad json')
        mock_get.return_value = mock_resp
        client = APIClient()
        with self.assertRaises(ValueError):
            client.fetch_data('http://example.com')

if __name__ == '__main__':
    unittest.main() 