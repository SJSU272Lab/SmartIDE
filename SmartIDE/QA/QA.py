#!/usr/bin/python

from flask import Flask, request, Response, json, abort
import requests
import lib.seq2seq_attention as seq2seq

app = Flask(__name__)


# start the QA server


vocab_path = "vocab/qa-vocab"
model_path = "model/model.ckpt-54311"
test = seq2seq.RNN_Decoder(vocab_path, model_path)
    

@app.route('/qa/<keyword>', methods = ['GET'])
def api_GET_PUT_DELETE(keyword):
    if request.method == 'GET':

        js = ""
        if(keyword != ""):
            keyword = keyword.replace("---", ' ')
            Question, Answer = test.Decode(keyword)
            js = { "QA": {"Question": Question, "Answer": Answer}}            

        #js_dic = { "postID": postID } 
        #js = json.dumps(js_dic)
        resp = Response(json.dumps(js), status=200, mimetype='application/json')
        #resp = Response(status=200)
        return resp




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2666, debug=True)
