#!/usr/bin/python
import lib.seq2seq_attention as SEQ

vocab_path = "vocab/qa-vocab"
model_path = "model/model.ckpt-54311"
test = SEQ.RNN_Decoder(vocab_path, model_path)

#Question, Answer = test.Decode("What's the difference betweem java class and java interface?")
Question, Answer = test.Decode("stackoverflow")
print "<Question>"+Question
print "<Answer>"+Answer
