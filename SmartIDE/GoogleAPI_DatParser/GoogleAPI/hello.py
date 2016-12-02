from flask import Flask, abort, request 
import json

app = Flask(__name__)


@app.route('/foo', methods=['POST', 'GET']) 
def search():
	if request.method == 'POST':
		print request.json.get('userId')
		return json.dumps(request.json)
	elif request.method == 'GET':
		select = request.args['userId']
    	return str(select)


# @app.route('/foo/<keyword>', methods=['GET']) 
# def get_search(keyword):
# 	if request.method == 'GET':
# 		print keyword
# 		return keyword


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)