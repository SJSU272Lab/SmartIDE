var Record = require('../models/record');
var res = {};

function retrieveRecord_request(msg, callback){
	console.log("In handle retrieveRecord request:"+ msg.question);
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
				res.code = "400";
				callback(null, res);
			}
		}
	});
	
}

function insertRecord_Request(msg, callback){
	console.log("In handle insertRecord request " + msg);
	var newRecord = new Record();
	newRecord.question = msg.question;
	newRecord.answer = msg.answer;
	newRecord.link = msg.link;
	newRecord.save(function(err){
		console.log("In record save");
		if(err){
			throw err;
		}else{
			console.log("In record if save");
			res.code = "200";
			callback(null, res);
		}
	});
}

function updateRecord_Request(msg, callback){
	console.log("In update request handle " + msg.id);
	Record.findByIdAndUpdate(msg.id, { $inc : { votes: 1 } }, {new:true}, function(err, result){
		if(err){
			throw err;
		}else{
			console.log("Result of update " + result);
			if(result != ''){
				res.code = '200';
				callback(null, res);
			}else{
				res.code = '400';
				callback(null,res);
			}
		}
	});
}

exports.retrieveRecord_request = retrieveRecord_request;
exports.insertRecord_Request = insertRecord_Request;
exports.updateRecord_Request = updateRecord_Request;