import json
import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        uuid_regex = "[0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}"
        print("testing response.")
        result = index.handler(None, None)
        json_body = json.loads(result['body'])
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertRegex(json_body['uuid'], uuid_regex, 'The returned value did not match the UUID pattern')


if __name__ == '__main__':
    unittest.main()
