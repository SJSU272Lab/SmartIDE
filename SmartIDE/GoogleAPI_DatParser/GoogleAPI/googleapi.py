
import os
from flask import Flask, jsonify, url_for, request, Response
from pprint import pprint
import json
from googleapiclient.discovery import build
from googleresult import *
import rake
import operator


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

# google custom search api and return json format
def searchfor(keyword):
    mykey = "AIzaSyCu3pFBOYTitLS1GyRm5TGeAstDDt3fAl8"
    service = build("customsearch", "v1", developerKey = mykey)
    res = service.cse().list(
        q = keyword,
        lr = 'lang_en',
        num = '5',
        cx = '011247095799164362687:htc6tt21zii',
        ).execute()
    # print json.dumps(res, indent = 4)
    return res

# search google results and parse those results
def cleanresult(result):
    clean = {"result": []}
    paragraph = ""
    for item in result.get("items"):
        # print json.dumps(item, indent = 4)
        ggresult = None
        if(item.get("pagemap").get("qapage") != None and item.get("pagemap").get("answer") != None):
            link = item.get("link")
            # print link
            question = item.get("pagemap").get("qapage")[0].get("name")
            ggresult = googleresult(question, link)
        if ggresult != None:
            clean["result"].append(ggresult.get_dict())
            paragraph += ggresult.get_ques() + " "
            '''
            concatenate entire answer paragraph and use it for searching keywords
            
            if ggresult.get_paragraph() != None:
                paragraph += ggresult.get_paragraph()
            '''
    clean["keywords"] = get_keywords(paragraph)
    return clean

# use rake to generate 5 keywords at most
def get_keywords(paragraph):
    kw_result = []
    rake_object = rake.Rake("SmartStoplist.txt", 3, 1, 1)
    keywords = rake_object.run(paragraph)
    for word in keywords:
        kw_result.append(word[0])
        if(len(kw_result) == 5): break
    return kw_result

# test if json format
# def is_json(myjson):
#     try:
#         json_object = json.loads(myjson)
#     except ValueError, e:
#         return False
#     return True

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=4000, debug=True)

