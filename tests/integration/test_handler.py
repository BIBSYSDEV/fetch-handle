import unittest

import boto3
import botocore

from tests.set_up_sam_local import SetUpSamLocal


class TestHandlerCase(unittest.TestCase):
    sam_local = None

    @classmethod
    def setUpClass(cls):
        cls.sam_local = SetUpSamLocal()
        cls.sam_local.set_up()

    @classmethod
    def tearDownClass(cls):
        cls.sam_local.tear_down()

    def test_response(self):
        lambda_client = boto3.client('lambda',
                                     region_name="eu-west-1",
                                     endpoint_url="http://127.0.0.1:3000",
                                     use_ssl=False,
                                     verify=False,
                                     config=botocore.client.Config(
                                         signature_version=botocore.UNSIGNED,
                                         read_timeout=2000,
                                         retries={'max_attempts': 0},
                                     )
                                     )

        # Invoke your Lambda function as you normally usually do. The function will run
        # locally if it is configured to do so
        response = lambda_client.invoke(FunctionName="FetchHandle")

        # Verify the response
        assert response == "Hello World"


if __name__ == '__main__':
    unittest.main()
