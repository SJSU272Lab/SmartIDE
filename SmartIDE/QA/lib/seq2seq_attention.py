# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import sys
import time

import tensorflow as tf
import data
import seq2seq_attention_decode
import seq2seq_attention_model

ckpt_path = 'model/model.ckpt-54311'
vocab_path = 'vocab/qa-vocab'
random_seed = 111
num_gpus = 0


def main(unused_argv):
  vocab = data.Vocab(vocab_path, 50000)#1000000
  # Check for presence of required special tokens.
  assert vocab.WordToId(data.PAD_TOKEN) > 0
  assert vocab.WordToId(data.UNKNOWN_TOKEN) >= 0
  assert vocab.WordToId(data.SENTENCE_START) > 0
  assert vocab.WordToId(data.SENTENCE_END) > 0



  hps = seq2seq_attention_model.HParams(
      mode='decode',  # train, eval, decode
      min_lr=0.01,  # min learning rate.
      lr=0.15,  # learning rate
      batch_size=4,
      enc_layers=4,
      enc_timesteps=120,
      dec_timesteps=30,
      min_input_len=2,  # discard articles/summaries < than this
      num_hidden=256,  # for rnn cell
      emb_dim=128,  # If 0, don't use embedding
      max_grad_norm=2,
      num_softmax_samples=4096)  # If 0, no sampled softmax.

  tf.set_random_seed(random_seed)

  decode_mdl_hps = hps

  print "Initializing..."
  decode_mdl_hps = hps._replace(dec_timesteps=1)
  model = seq2seq_attention_model.Seq2SeqAttentionModel(decode_mdl_hps, vocab, num_gpus)
  print "Finish Initiailizing"

  #loading model
  decoder = seq2seq_attention_decode.BSDecoder(model, hps, vocab, ckpt_path)


  print "==============================================="
  Question, Answer = decoder._Decode("What's the difference betweem java class and java interface?")
  print "<Question>"+Question
  print "<Answer>"+Answer
  Question, Answer = decoder._Decode("Why does it show the error message, stackoverflow?")
  print "<Question>"+Question
  print "<Answer>"+Answer
  print "+++++++++++++++++++++++++++++++++++++++++"


if __name__ == '__main__':
  tf.app.run()
