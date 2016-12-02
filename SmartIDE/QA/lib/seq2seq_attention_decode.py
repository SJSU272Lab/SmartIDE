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

"""Module for decoding."""

import os
import time

import tensorflow as tf
import beam_search
import data


DECODE_LOOP_DELAY_SECS = 60
DECODE_IO_FLUSH_INTERVAL = 100


class BSDecoder(object):
  """Beam search decoder."""

  def __init__(self, model, hps, vocab, ckpt_name):
    """Beam search decoding.
    Args:
      model: The seq2seq attentional model.
      batch_reader: The batch data reader.
      hps: Hyperparamters.
      vocab: Vocabulary
    """
    self._model = model
    print "--- Start Loading Graph... ---"
    self._model.build_graph()
    print "--- Finish Loading Graph ---"
    self._hps = hps
    self._vocab = vocab
    self._saver = tf.train.Saver()
    self._ckpt_name = ckpt_name
    ########## loading model ############
    print "--- Start Loading Model..... ---"
    self._sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))

    self._saver.restore(self._sess, self._ckpt_name)

    print "--- Finish Loading Model ---"
    #####################################





  def _Decode(self, article_text):
    """Restore a checkpoint and decode it.
    Args:
      saver: Tensorflow checkpoint saver.
      sess: Tensorflow session.
    Returns:
      If success, returns true, otherwise, false.
    """

    bs = beam_search.BeamSearch(
        self._model, self._hps.batch_size,
        self._vocab.WordToId(data.SENTENCE_START),
        self._vocab.WordToId(data.SENTENCE_END),
        self._hps.dec_timesteps)

    ###################
    #article_text = "How do I know the difference, between class and object"
    article = "<d><p><s>"+article_text+"</s></p></d>"
    article_sentences = [sent.strip() for sent in data.ToSentences(article, include_token=False)]
    pad_id = self._vocab.WordToId(data.PAD_TOKEN)

    enc_inputs = []
    for i in xrange(min(100,len(article_sentences))):
      enc_inputs += data.GetWordIds(article_sentences[i], self._vocab)

    enc_input_len = len(enc_inputs)
    while len(enc_inputs) < self._hps.enc_timesteps:
      enc_inputs.append(pad_id)
    ###################


    w, h = 120, 4
    article_batch_cp = [[0 for x in range(w)] for y in range(h)] 
    for i in range(0,4):
      article_batch_cp[i] = enc_inputs#article_batch[i]


    w, h = 1, 4
    article_lens_cp = [[0 for x in range(w)] for y in range(h)] 
    #article_lens_cp = article_lens.copy()
    for i in range(0,4):
      article_lens_cp[i] = enc_input_len

    best_beam = bs.BeamSearch(self._sess, article_batch_cp, article_lens_cp)
    #print len(best_beam)
    best_beam = best_beam[0]
     
    decode_output = [int(t) for t in best_beam.tokens[1:]]

    QUESTION = article_text

    test = ' '.join(data.Ids2Words(decode_output, self._vocab))
    end_p = test.find(data.SENTENCE_END, 0)

    if end_p != -1:
      test = test[:end_p]
    #print "<Answer>"+test
    ANSWER = test.replace('<UNK>','')

    return QUESTION, ANSWER

