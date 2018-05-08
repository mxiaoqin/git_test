import unittest
import sys
import os
import requests
import json

patch = os.path.dirname(os.path.realpath(__file__))
patch = patch[0:patch.rfind('\\')]
sys.path.append(patch)


class Test_xc_pc_index(unittest.TestCase):
    def setUp(self):
        self.headers = {'Accept': 'application/json'}
        self.cookies = ''
        self.url = 'http://192.168.1.203:9098/teacher/login'
        print('start')

    def test_xc_pc_index(self):
        data = {}
        data["mobile"] = "l_002"
        data['password'] = "666666"
        data['keepPassword'] = ""

        r = requests.post(self.url,data,self.headers)
        print(str(r.status_code))
        print(r.text)


    def tearDown(self):
        print('end')


if __name__ == '__main__':
    unittest.main()

