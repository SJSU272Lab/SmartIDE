/**var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var recordSchema = new Schema({
	question: {type: String, required: true},
	answer: {type: String, required: true}
});

module.exports = mongoose.model('Record', recordSchema);**/