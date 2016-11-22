#!/usr/bin/python

from flask import Flask, request, Response, json, abort
import requests

app = Flask(__name__)


@app.route('/controller/<keyword>', methods = ['GET', 'PUT', 'DELETE'])
def api_GET_PUT_DELETE(keyword):
    if request.method == 'GET':

        #if request.headers['Content-Type'] != 'application/json':
        #    abort(404)

        #First, check the database
        r_db = requests.get('http://localhost:3000/insertRecord')
        print r_db.text
        #Then, search the google 
        r_google = requests.get('http://localhost:4000/search?question=%s'%keyword)


        dictA = json.loads(r_db.text)
        dictB = json.loads(r_google.text)

        merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}

        # string dump of the merged dict
        r = json.dumps(merged_dict)



        js = r
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


@app.route('/controller', methods = ['POST'])
def api_POST():
    if request.method == 'POST':    

        if request.headers['Content-Type'] != 'application/json':
            abort(404)

        resp_dict = json.loads(request.data)
   
        js = json.dumps(resp_dict)

        #print js
        #print json.loads(js)
        resp = Response(js, status=201, mimetype='application/json')
        return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1314, debug=True)
