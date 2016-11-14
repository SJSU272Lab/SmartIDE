#!/usr/bin/python

from flask import Flask, request, Response, json, abort

app = Flask(__name__)


@app.route('/controller/<int:postID>', methods = ['GET', 'PUT', 'DELETE'])
def api_GET_PUT_DELETE(postID):
    if request.method == 'GET':

        if request.headers['Content-Type'] != 'application/json':
            abort(404)

        js_dic = { "postID": postID } 
        js = json.dumps(js_dic)
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
