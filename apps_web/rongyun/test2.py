#! /usr/bin/env python
# coding=utf-8

import json
import logging
import os
import unittest

from rongyun import api


#app_key = ""
#app_secret = ""
#os.environ.setdefault('rongcloud_app_key', app_key)
#os.environ.setdefault('rongcloud_app_secret', app_secret)
logging.basicConfig(level=logging.INFO)

client = api.getRongyun()


class ApiTest(unittest.TestCase):
    def test_message_system_publish(self):
        result = client.message_system_publish(
            from_user_id=1,#'test-userid1',
            to_user_id=[1,89],
            object_name='RC:TxtMsg',
            content=json.dumps({"content":"hello"}),
            push_content='thisisapush',
            push_data='aa')
        
        print result
        self.assertEqual(result[u'code'], 200)

if __name__ == "__main__":
    unittest.main()