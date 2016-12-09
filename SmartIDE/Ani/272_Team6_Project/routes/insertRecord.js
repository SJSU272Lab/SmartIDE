var express = require('express');
var router = express.Router();
var mq_client = require('../rpc/client');

/* POST insert */
router.post('/', function(req, res, next) {
	var json_responses = '';
	var keyword = req.body.keyword;
	var newAnswer = req.body.answer;
	var question = req.body.question;
	var link = req.body.link; 
	var vote = req.body.vote;
	var msg_payload = {"keyword": keyword, "answer": newAnswer, "link": link, "votes": vote, "question": question};
	
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
