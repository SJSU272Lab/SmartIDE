var express = require('express');
var router = express.Router();
var mq_client = require('../rpc/client');

/* GET home page. */
router.get('/', function(req, res, next) {
	var json_responses = '';
	var id = '583b868b424a6e217cf4b1bd';
	var msg_payload = {"id": id};
	
	mq_client.make_request('updateRecord_queue',msg_payload, function(err,results){
		console.log(results);
		if(err){
			throw err;
		}else{
			if(results.code === '200'){
				console.log("Answers "+results.value);
				json_responses = {'statusCode': '200', 'message': 'Vote count updated Successfully!'};
				res.send(json_responses);
			}else{
				json_responses = {'statusCode': '400', 'message': 'Something went wrong!'};
				res.send(json_responses);
			}
		}
	});
});

module.exports = router;
