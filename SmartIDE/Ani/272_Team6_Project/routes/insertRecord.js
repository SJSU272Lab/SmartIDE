var express = require('express');
var router = express.Router();
var mq_client = require('../rpc/client');

/* GET home page. */
router.get('/', function(req, res, next) {
	var json_responses = '';
	var newQuestion = 'Mongoose promise error';
	var newAnswer = "With mongoose@4.1 you can use any promises that you want var mongoose = require('mongoose'); mongoose.Promise = require('bluebird');";
	var link = "http://www.stackoverflow.com/"; 
	var msg_payload = {"question": newQuestion, "answer": newAnswer, "link": link};
	
	mq_client.make_request('insertRecord_queue',msg_payload, function(err,results){
		console.log(results);
		if(err){
			throw err;
		}else{
			if(results.code === '200'){
				console.log("Answers "+results.value);
				json_responses = {'statusCode': '200', 'message': 'Stored Question Answer Pair Successfully!'};
				res.send(json_responses);
			}else{
				json_responses = {'statusCode': '400', 'message': 'Something went wrong!'};
				res.send(json_responses);
			}
		}
	});
});

module.exports = router;
