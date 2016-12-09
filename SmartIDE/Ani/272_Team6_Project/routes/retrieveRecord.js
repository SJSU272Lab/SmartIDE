var express = require('express');
var router = express.Router();
var mq_client = require('../rpc/client');

/* POST home page. */
router.post('/', function(req, res, next) {
	var json_responses = '';
	var newQuestion = req.body.keyword;
	var quesArray = newQuestion.split('+');
	console.log("Keywords to be searched "+quesArray);
	var msg_payload = {"question": quesArray};
	mq_client.make_request('retrieveRecord_queue',msg_payload, function(err,results){
		console.log(results);
		if(err){
			throw err;
		}else{
			if(results.code === '200'){
				//console.log("Answers "+results.value);
				json_responses = {'statusCode': '200', 'message': results.value};
				res.send(json_responses);
			}else{
				json_responses = {'statusCode': '400', 'message': 'answer not found in the database'};
				res.send(json_responses);
			}
		}
	});
});

module.exports = router;