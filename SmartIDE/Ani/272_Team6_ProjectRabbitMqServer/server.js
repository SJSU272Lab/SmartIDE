//super simple rpc server example
var amqp = require('amqp');
var util = require('util');
var mongoose = require('mongoose');
var retrieveRecord = require('./services/retrieveRecord');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://mongodb/record');

var cnn = amqp.createConnection({host:'smartide-rabbit'});

cnn.on('ready', function(){
	console.log("listening on queue");
	
	cnn.queue('retrieveRecord_queue', function(q){
		q.subscribe(function(message, headers, deliveryInfo, m){
			util.log(util.format( deliveryInfo.routingKey, message));
			util.log("Message: "+JSON.stringify(message));
			util.log("DeliveryInfo: "+JSON.stringify(deliveryInfo));
			retrieveRecord.retrieveRecord_request(message, function(err,res){

				//return index sent
				cnn.publish(m.replyTo, res, {
					contentType:'application/json',
					contentEncoding:'utf-8',
					correlationId:m.correlationId
				});
			});
		});
	});
});