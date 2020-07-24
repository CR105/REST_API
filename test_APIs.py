import requestAPI
from datetime import datetime
from collections import Counter
import json
import os
import zipfile

with open(r'/Users/carios/Documents/workspace_Python/REST_API/datapool.json', encoding="utf-8") as f:
    jData = json.load(f)

my_token = requestAPI.getToken(jData["uri_Auth"], jData["userCatalyst"], jData["passCatalyst"])
exePath = r'/Users/carios/Documents/workspace_Python/REST_API/Evidence/' + datetime.today().strftime('%Y%m%d%H%M%S')
os.mkdir(exePath)

# enviar( Str Name EndPoint, json data, object token, str metodo, str código de respuesta)
list_result = []
list_result.append(requestAPI.customAPIRequest("search" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("retrieve_balance" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("retrieve_movements" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("retrieve_movement_detail" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("persons" ,jData, my_token, "POST", "422", exePath))
list_result.append(requestAPI.customAPIRequest("curp_validate" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("curp_compare" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("curp_search" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("rfc" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("ine_validate" ,jData, my_token, "POST", "200", exePath))
list_result.append(requestAPI.customAPIRequest("validate" ,jData, my_token, "POST", "200", exePath))

filesPath = []
for root, directories, files in os.walk(exePath):
    for filename in files:
        filePath = os.path.join(root, filename)
        filesPath.append(filePath)
        
zip_file = zipfile.ZipFile(exePath +'/Result.zip', 'w')
with zip_file:
    for filesName in filesPath:
        zip_file.write(filesName)

exeResult = Counter(list_result)
print("Total ejecutados:", len(list_result))
if True in exeResult:
    print("Pasados:", exeResult[True], ",", round((exeResult[True]/len(list_result))*100,2), "%")
else:
    print("Pasados:", 0, ",", round((0/len(list_result))*100,2), "%")
if False in exeResult:
    print("Fallados:", exeResult[False], ",", round((exeResult[False]/len(list_result))*100,2), "%")
else:
    print("Fallados:", 0, ",", round((0/len(list_result))*100,2), "%")

