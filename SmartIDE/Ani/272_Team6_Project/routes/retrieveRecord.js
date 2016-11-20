var express = require('express');
var router = express.Router();
var mq_client = require('../rpc/client');
//var Record = require('../models/record');

/* GET home page. */
router.get('/', function(req, res, next) {
	var json_responses = '';
	var newQuestion = 'Mongoose promise error';
	var newAnswer = "With mongoose@4.1 you can use any promises that you want var mongoose = require('mongoose'); mongoose.Promise = require('bluebird');";
	var msg_payload = {"question": newQuestion, "answer": newAnswer};
	
	mq_client.make_request('retrieveRecord_queue',msg_payload, function(err,results){
		
		console.log(results);
		if(err){
			throw err;
		}else{
			if(results.code === '200'){
				console.log("Orders "+results.value);
				json_responses = {'statusCode': '200', 'message': results.value};
				res.send(json_responses);
			}else if(results.code === '201'){
				json_responses = {'statusCode': '201', 'message': 'New answer inserted for question ' + newQuestion};
				res.send(json_responses);
			}
		}
	});
	
	/**Record.find({question: newQuestion}, function(err, result){
		console.log("In record find");
		if(err){
			throw err;
		}
		else{
			if(result != ""){
				console.log("In record if found");
				json_responses = {'statusCode': '200','message': result};
				res.send(json_responses);
			}else{
				var newRecord = new Record();
				newRecord.question = newQuestion;
				newRecord.answer = "With mongoose@4.1 you can use any promises that you want var mongoose = require('mongoose'); mongoose.Promise = require('bluebird');";
				newRecord.save(function(err){
					console.log("In record save");
					if(err){
						throw err;
					}else{
						console.log("In record if save");
						json_responses = {'statusCode': '201','message': 'New answer inserted for question ' + newQuestion};
						res.send(json_responses);
					}
				});
			}
		}
	});**/
});

module.exports = router;