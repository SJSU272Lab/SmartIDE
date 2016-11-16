var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	var json_responses = '';
	json_responses = {'statusCode': '200','message': 'You are in delete record'};
	res.send(json_responses);
});

module.exports = router;
