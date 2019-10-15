import json
import unittest

from src import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        uuid_regex = "[0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}"
        print("testing response.")

        event = {
            'body': '{"url": "https://unit.no"}'
        }

        result = index.handler(event, None)
        json_body = json.loads(result['body'])
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertRegex(json_body['uuid'], uuid_regex, 'The returned value did not match the UUID pattern')
        self.assertEqual('https://unit.no', json_body['inputUrl'])

    def test_error_response(self):

        event = {
            'body': '{"url": "unit.no"}'
        }

        result = index.handler(event, None)
        json_body = json.loads(result['body'])
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertNotEqual(json_body['inputUrl'], 'https://unit.no')
        self.assertIsNone(json_body['inputUrl'])


if __name__ == '__main__':
    unittest.main()
