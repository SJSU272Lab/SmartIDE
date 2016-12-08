var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var recordSchema = new Schema({
	keyword: {type: [String], required: true},
	answer: {type: String, required: true},
	question: {type: String},
	link: {type:String}, 
	votes : {type:Number, default:0},
	created: {type:Date, default: Date.now}
});

module.exports = mongoose.model('Record', recordSchema);