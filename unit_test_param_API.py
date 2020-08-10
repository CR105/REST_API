import csv
import json
import unittest
import os
import zipfile
import requestAPI
from collections import Counter
from datetime import datetime
from docx import Document
from parameterized import parameterized

event = []
endP = []
pathResource = '/Users/carios/Documents/workspace_Python/REST_API/resource/' #'C:\\Projects_Python\\Rest_API\\resources\\'
pathEvidence = '/Users/carios/Documents/workspace_Python/REST_API/evidence/' #r'C:\\Projects_Python\\Rest_API\\Evidence\\'

def data():
    dataPool = []
    with open(pathResource + '/datapool.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dataPool.append(tuple(row))
    return dataPool

class test_API(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open(pathResource + 'data.json', encoding="utf-8") as f:
            cls.data = json.load(f)
        cls.token = requestAPI.getToken(cls.data["uri_Auth"], cls.data["userCatalyst"], cls.data["passCatalyst"])
        cls.pathExe = pathEvidence + datetime.today().strftime('%Y%m%d%H%M%S')
        os.mkdir(cls.pathExe)
        print("\nCargando datos...")
        cls.startTime = datetime.today()
    
    @classmethod
    def tearDownClass(cls):
        requestAPI.zipingResults(cls.pathExe, 'Result.zip')
        requestAPI.report(cls.data, event, endP, pathResource, cls.pathExe, str(datetime.today() - cls.startTime))
    
    @parameterized.expand(data())
    def test_serch(self, strNameEndPoint, method, expectReturnCode):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest(strNameEndPoint ,jData, my_token, method, expectReturnCode, exePath)
        event.append(test)
        endP.append([strNameEndPoint, rc])
        self.assertTrue(test)

runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(test_API)
runner.run(suite)