#!/usr/bin/python

from flask import Flask, request, Response, json, abort
import requests

app = Flask(__name__)





@app.route('/qa/<keyword>', methods = ['GET'])
def api_GET_PUT_DELETE(keyword):
    if request.method == 'GET':








        js = ""
        #js_dic = { "postID": postID } 
        #js = json.dumps(js_dic)
        resp = Response(js, status=200, mimetype='application/json')
        #resp = Response(status=200)
        return resp




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2666, debug=True)
