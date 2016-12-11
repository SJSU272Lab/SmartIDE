#!/usr/bin/python

from flask import Flask, request, Response, json, abort
import requests

app = Flask(__name__)


## need to have mechanism to remove the duplicate between   DB   and   GOOGLE
def mergeDict(dictA, dictB, dictC):
    dictC_result = [{ "answer":dictC["QA"]["Answer"], "question":dictC["QA"]["Question"] }]
    dictB_result = dictB
    dictA_result = dictA["result"]

    print dictB_result[0]

    merged_result = []
    merged_result.extend(dictC_result)
    merged_result.extend(dictB_result)
    merged_result.extend(dictA_result)

    merged_dict = {
        "keywords":dictA["keywords"],
        "question":dictA["question"],
        "result": merged_result
    }
    return merged_dict


@app.route('/controller/<keyword>', methods = ['GET', 'PUT', 'DELETE'])
def api_GET_PUT_DELETE(keyword):
    if request.method == 'GET':

        #if request.headers['Content-Type'] != 'application/json':
        #    abort(404)


        #First, search the google 
        r_google = requests.get('http://localhost:4000/search?question=%s'%keyword)
        dictA = json.loads(r_google.text)
        dictA["question"] =  keyword.replace("---", " ")
        #print dictA
        
        #Then, check the database by using the keyword google gave
        keyword_list = dictA["keywords"]
        keyword_str = ""
        for i in range(0,len(keyword_list)):
            keyword_str += keyword_list[i]
            if i < len(keyword_list)-1:
                keyword_str += "+"
        msg_payload_dic = {"keyword":keyword_str}
        msg_payload = json.dumps(msg_payload_dic)
        #print msg_payload
        r_db = requests.post('http://localhost:3000/retrieveRecord', data=msg_payload_dic)
        #print r_db.text
        dictB = json.loads(r_db.text)
        #print dictB

        dictB_extract = []
        for i in range(0,len(dictB["message"])):
            dictB_extract.append({ 
                "id": dictB["message"][i]["_id"],
                "answer": dictB["message"][i]["answer"],
                "link": dictB["message"][i]["link"],
                "question": dictB["message"][i]["question"],
                "vote": dictB["message"][i]["votes"]
            })
        #print dictB_extract


        #Then, search the QA system
        r_QA = requests.get('http://localhost:2666/qa/%s'%keyword)
        dictC = json.loads(r_QA.text)
        #print dictC
        




        ## need to have mechanism to remove the duplicate between   DB   and   GOOGLE
        ## need to have mechanism to remove the duplicate between   DB   and   GOOGLE
        ## need to have mechanism to remove the duplicate between   DB   and   GOOGLE
        
        #merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items() + dictC.items() )}
        merged_dict_test = mergeDict(dictA, dictB_extract, dictC)
        #print merged_dict_test

        # string dump of the merged dict
        #r = json.dumps(merged_dict)
        r = json.dumps(merged_dict_test)

        js = r
        #print js
        #js_dic = { "postID": postID } 
        #js = json.dumps(js_dic)
        resp = Response(js, status=200, mimetype='application/json')
        #resp = Response(status=200)
        return resp


    elif request.method == 'PUT':
        if request.headers['Content-Type'] != 'application/json':
            abort(404)

        resp = Response(status=202)
        return resp
        


    elif request.method == 'DELETE':
        if request.headers['Content-Type'] != 'application/json':
            abort(404)

        resp = Response(status=204)
        return resp


@app.route('/controller/', methods = ['POST'])
def api_POST():
    if request.method == 'POST':    

        if request.headers['Content-Type'] != 'application/json':
            abort(404)

        resp_dict = json.loads(request.data)
        print resp_dict

        # ## unmarshal the post request
        
        # Answer is from db ---> UPDATE
        if "id" in resp_dict["result"][0]:
            print "!!!!!!!!!!!!!!! Answer is from db"
            msg_payload_dic = {
                "id":resp_dict["result"][0],
                "vote": resp_dict["result"][0]["vote"]
            }
            #insert it into DB
            r_db = requests.post('http://localhost:3000/updateRecord', data=msg_payload_dic)

        # Answer is from google ---> INSERT
        elif "link" in resp_dict["result"][0]:
            print "!!!!!!!!!!!!!!! Answer is from google"
            msg_payload_dic = {
                "keyword": resp_dict["keywords"],
                "question": resp_dict["result"][0]["question"], 
                "answer": resp_dict["result"][0]["answer"], 
                "vote": resp_dict["result"][0]["vote"], 
                "link": resp_dict["result"][0]["link"]         
            }
            #insert it into DB
            r_db = requests.post('http://localhost:3000/insertRecord', data=msg_payload_dic)

        # Answer is from google ---> INSERT
        elif "question" in resp_dict["result"][0]:
            print "!!!!!!!!!!!!!!! Answer is from QA"
            msg_payload_dic = {
                "keyword": resp_dict["keywords"],
                "question": resp_dict["result"][0]["question"], 
                "answer": resp_dict["result"][0]["answer"], 
                "vote": resp_dict["result"][0]["vote"],    
                "link": ""    
            }
            print msg_payload_dic
            #insert it into DB
            r_db = requests.post('http://localhost:3000/insertRecord', data=msg_payload_dic)

        print r_db.text
        # msg_payload_dic = {
        #     "keyword": resp_dict["keywords"],
        #     "question": resp_dict["result"][0]["question"], 
        #     "answer": resp_dict["result"][0]["answer"], 
        #     "votes": resp_dict["result"][0]["vote"], 
        #     "link": resp_dict["result"][0]["link"]         
        # }


        #insert it into DB
        #r_db = requests.post('http://localhost:3000/insertRecord', data=msg_payload_dic)

        js = json.dumps(resp_dict)
        #print js


        resp = Response(js, status=201, mimetype='application/json')
        return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1314, debug=True)
