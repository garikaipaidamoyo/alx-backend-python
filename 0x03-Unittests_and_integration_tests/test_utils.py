#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([({
        "a": 1
    }, ("a", ), 1), ({
        "a": {
            "b": 2
        }
    }, ("a", ), {
        "b": 2
    }), ({
        "a": {
            "b": 2
        }
    }, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([({}, ("a", ), KeyError("a")),
                           ({
                               "a": 1
                           }, ("a", "b"), KeyError("b"))])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        with self.assertRaises(type(expected_exception)) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))


class TestGetJson(unittest.TestCase):

    @parameterized.expand([("http://example.com", {
        "payload": True
    }), ("http://holberton.io", {
        "payload": False
    })])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        test_instance = self.TestClass()
        with patch.object(test_instance, 'a_method') as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            mock_method.assert_called_once()
            self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
