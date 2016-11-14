
import os
from flask import Flask, jsonify, url_for, request, Response
from pprint import pprint
import json
from googleapiclient.discovery import build
from googleresult import *

app = Flask(__name__)

@app.route('/<keyword>', methods = ['GET'])
def api_search(keyword):
    result = searchfor(keyword)
    clean = cleanresult(result)
    return jsonify(**clean)

def searchfor(keyword):
    mykey = "AIzaSyCu3pFBOYTitLS1GyRm5TGeAstDDt3fAl8"
    service = build("customsearch", "v1", developerKey = mykey)
    res = service.cse().list(
        q = keyword,
        lr = 'lang_en',
        num = '5',
        cx = '011247095799164362687:htc6tt21zii',
        ).execute()
    return res

def cleanresult(result):
    clean = {"result": []}
    # print is_json(result)
    for item in result.get("items"):
        link = item.get("link")
        # print link
        if(item.get("pagemap").get("qapage") != None):
            question = item.get("pagemap").get("qapage")[0].get("name")
        else:
            question = "no question"
        ggresult = googleresult(question, link)
        clean["result"].append(ggresult.get_dict())
    return clean

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False
    return True

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

