#!/usr/bin/python
import seq2seq_attention


test = seq2seq_attention.RNN_Decoder()
Question, Answer = test.Decode("What's the difference betweem java class and java interface?")
print "<Question>"+Question
print "<Answer>"+Answer
#Question, Answer = test.Decode("Why does it show the error message, stackoverflow?")
#print "<Question>"+Question
#print "<Answer>"+Answer