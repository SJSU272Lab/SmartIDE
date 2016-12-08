var Record = require('../models/record');
//var _ = require('underscore');
var res = {};

function sortUsing(property){
    return function(a, b){
        if(a[property] < b[property]){
            return 1;
        }else if(a[property] > b[property]){
            return -1;
        }else{
            return 0;   
        }
    }
}

function retrieveRecord_request(msg, callback){
	console.log("In handle retrieveRecord request:"+ msg.question);
	var answersArray = [];
	var itemsProcessed = 0;
	msg.question.forEach(function(question){
		Record.find({keyword: question}, function(err, result){
			console.log("In record find");
			if(err){
				throw err;
			}
			else{
				itemsProcessed++;
				result.forEach(function(answer){
					answersArray.push(answer);
				});
				if(itemsProcessed == msg.question.length){
					answersArray.sort(sortUsing("votes"));
					res.code='200';
					res.value=answersArray;
					callback(null,res);
				}
			}
		});
	});
}

function insertRecord_Request(msg, callback){
	console.log("In handle insertRecord request " + msg);
	var newRecord = new Record();
	newRecord.keyword = msg.keyword;
	newRecord.votes = msg.votes;
	console.log("msg.votes");
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