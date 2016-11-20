var Record = require('../models/record');

function retrieveRecord_request(msg, callback){
	
	var res = {};
	console.log("In handle retrieveRecord request:"+ msg.question);
	var json_responses ='';
	Record.find({question: msg.question}, function(err, result){
		console.log("In record find");
		if(err){
			throw err;
		}
		else{
			if(result != ""){
				console.log("In record if found");
				res.code = "200";
				res.value = result;
				callback(null, res);
			}else{
				var newRecord = new Record();
				newRecord.question = msg.question;
				newRecord.answer = msg.answer;
				newRecord.save(function(err){
					console.log("In record save");
					if(err){
						throw err;
					}else{
						console.log("In record if save");
						res.code = "201";
						callback(null, res);
					}
				});
			}
		}
	});
	
}

exports.retrieveRecord_request = retrieveRecord_request;