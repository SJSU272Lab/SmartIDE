#!/usr/bin/python

from flask import Flask, request, Response, json, abort
import requests

app = Flask(__name__)


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



        #Then, search the QA system
        r_QA = requests.get('http://localhost:2666/qa/%s'%keyword)
        dictC = json.loads(r_QA.text)
        #print dictC
        




        ## need to have mechanism to remove the duplicate between   DB   and   GOOGLE
        ## need to have mechanism to remove the duplicate between   DB   and   GOOGLE
        ## need to have mechanism to remove the duplicate between   DB   and   GOOGLE
        merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items() + dictC.items() )}
        #merged_dict = {key: value for (key, value) in (dictB.items() + dictC.items() )}

        # string dump of the merged dict
        r = json.dumps(merged_dict)

        js = r
        print js
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
        
        # ## unmarshal the post request
        msg_payload_dic = {
             "keyword": resp_dict["keywords"],

            "question": resp_dict["result"][0]["question"], 
            "answer": resp_dict["result"][0]["answer"], 
            "votes": resp_dict["result"][0]["vote"] , 
            "link": resp_dict["result"][0]["link"]         
        }


        #insert it into DB
        r_db = requests.post('http://localhost:3000/insertRecord', data=msg_payload_dic)

        js = json.dumps(resp_dict)
        print js


        resp = Response(js, status=201, mimetype='application/json')
        return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1314, debug=True)
