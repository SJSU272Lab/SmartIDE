import json
from pprint import pprint
result = "/Users/BondK/Cloud/Dropbox/SJSU/CMPE272/Fall16-Team6/SmartIDE/GoogleAPI_DatParser/GoogleAPI/test_case1.json"

with open(result) as data_file:    
    result = json.load(data_file)

# pprint(data)

def cleanresult(result):
    for item in result.get("items"):
        if(item.get("pagemap").get("qapage") != None and item.get("pagemap").get("answer") != None):
            link = item.get("link")
            print link
            question = item.get("pagemap").get("qapage")[0].get("name")
            print question



cleanresult(result)