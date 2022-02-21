import unittest
from unittest import mock
import os, sys

class TestModel(unittest.TestCase):

    def setUp(self):
        currentdir = os.path.dirname(os.path.realpath(__file__))
        parentdir = os.path.dirname(currentdir)
        sys.path.append(parentdir)
        
    def test_handler(self):
        from lambda_function import app

        event = {
            'body': [
                {
                    's3': {
                        'bucket': {
                            'name': ''
                        },
                        'object': {
                            'key': ''
                        }
                    }
                }
            ]
        }

        result = app.handler(event, {})
        print(result)
        self.assertEqual(result, {'StatusCode': 200, 'body': '{32, 12, 2, 119.45, 1}'})

#python3 -m unittest discover
#coverage run -m pytest
