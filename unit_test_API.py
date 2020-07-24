import json
import unittest
import os
import zipfile
import requestAPI
from datetime import datetime
from collections import Counter
from docx import Document

event = []
endP = []
pathResource = '/Users/carios/Documents/workspace_Python/REST_API/resource/' #'C:\\Projects_Python\\Rest_API\\resources\\'
pathEvidence = '/Users/carios/Documents/workspace_Python/REST_API/evidence/' #r'C:\\Projects_Python\\Rest_API\\Evidence\\'

class API_test(unittest.TestCase):

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
        
    @unittest.skip("reason for skipping")
    def test_serch(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("search" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["search", rc])
        self.assertTrue(test)
    
    @unittest.skip("reason for skipping")
    def test_retrieve_balance(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("retrieve_balance" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["retrieve_balance", rc])
        self.assertTrue(test)
    
    @unittest.skip("reason for skipping")
    def test_retrieve_movements(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("retrieve_movements" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["retrieve_movements", rc])
        self.assertTrue(test)

    @unittest.skip("reason for skipping")
    def test_retrieve_movement_detail(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("retrieve_movement_detail" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["retrieve_movement_detail", rc])
        self.assertTrue(test)

    @unittest.skip("reason for skipping")
    def test_persons(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("persons" ,jData, my_token, "POST", "422", exePath)
        event.append(test)
        endP.append(["persons", rc])
        self.assertTrue(test)

    @unittest.skip("reason for skipping")
    def test_curp_validate(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("curp_validate" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["curp_validate", rc])
        self.assertTrue(test)

    # @unittest.skip("reason for skipping")
    def test_curp_compare(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("curp_compare" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["curp_compare", rc])
        self.assertTrue(test)

    # @unittest.skip("reason for skipping")
    def test_curp_search(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("curp_search" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["curp_search", rc])
        self.assertTrue(test)

    @unittest.skip("reason for skipping")
    def test_rfc(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("rfc" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["rfc", rc])
        self.assertTrue(test)

    @unittest.skip("reason for skipping")
    def test_ine_validate(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        
        test, rc = requestAPI.customAPIRequest("ine_validate" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["ine_validate", rc])
        self.assertTrue(test)

    @unittest.skip("reason for skipping")
    def test_validate(self):  
        jData = self.__class__.data
        my_token = self.__class__.token
        exePath = self.__class__.pathExe
        test, rc = requestAPI.customAPIRequest("validate" ,jData, my_token, "POST", "200", exePath)
        event.append(test)
        endP.append(["validate", rc])
        self.assertTrue(test)

# if __name__ == '__main__':
#     unittest.main()

runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(API_test)
runner.run(suite)