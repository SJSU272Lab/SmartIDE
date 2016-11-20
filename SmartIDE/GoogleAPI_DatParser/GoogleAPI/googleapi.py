
import os
from flask import Flask, jsonify, url_for, request, Response
from pprint import pprint
import json
from googleapiclient.discovery import build
from googleresult import *

app = Flask(__name__)

@app.route('/search', methods = ['GET', 'POST'])
def api_search():
    if request.method == 'POST':
        keyword = request.json.get("question")
        print keyword
    elif request.method == 'GET':
        keyword = request.args.get('question')

    if keyword == "None" or keyword == None:
        return "Keyword Missing"
    
    result = searchfor(keyword)
    clean = cleanresult(result)
    clean["question"] = keyword
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
    # print json.dumps(res, indent=4)
    return res

def cleanresult(result):
    clean = {"result": []}
    for item in result.get("items"):
        ggresult = None
        if(item.get("pagemap").get("qapage") != None and item.get("pagemap").get("answer") != None):
            link = item.get("link")
            # print link
            question = item.get("pagemap").get("qapage")[0].get("name")
            ggresult = googleresult(question, link)
        if ggresult != None:
            clean["result"].append(ggresult.get_dict())
    return clean

# def is_json(myjson):
#     try:
#         json_object = json.loads(myjson)
#     except ValueError, e:
#         return False
#     return True

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

