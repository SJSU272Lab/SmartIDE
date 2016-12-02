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
    print "0000000000000000000"
    self._model.build_graph()
    print "-------------------"
    self._hps = hps
    self._vocab = vocab
    self._saver = tf.train.Saver()
    self._ckpt_name = ckpt_name
    ########## loading model ############
    print "Start Loading Models....."
    self._sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
    #ckpt_path --> automatically lookup from check point
    #print ckpt_path
    ckpt_path_luckman = "model/model.ckpt-54311"
    self._saver.restore(self._sess, self._ckpt_name)

    print "Finish Loading Models"
    #####################################


    #print "1111111111111111111"
    #self._decode_io = DecodeIO(FLAGS.decode_dir)
    #print "2222222222222222222"




  def _Decode(self, article_text):
    """Restore a checkpoint and decode it.
    Args:
      saver: Tensorflow checkpoint saver.
      sess: Tensorflow session.
    Returns:
      If success, returns true, otherwise, false.
    """
    
    
    
    # print "''''''''''''''''''''''''''''''"
    # ckpt_state = tf.train.get_checkpoint_state(FLAGS.log_root)
    # if not (ckpt_state and ckpt_state.model_checkpoint_path):
    #   tf.logging.info('No model to decode yet at %s', FLAGS.log_root)
    #   return False

    # tf.logging.info('checkpoint path %s', ckpt_state.model_checkpoint_path)
    # ckpt_path = os.path.join(
    #     FLAGS.log_root, os.path.basename(ckpt_state.model_checkpoint_path))
    # tf.logging.info('renamed checkpoint path %s', ckpt_path)

    # #ckpt_path --> automatically lookup from check point
    # #print ckpt_path
    # ckpt_path_luckman = "log_root/model.ckpt-54311"
    # saver.restore(sess, ckpt_path_luckman)

    #self._decode_io.ResetFiles()

    #for _ in xrange(FLAGS.decode_batches_per_ckpt):
    #for _ in xrange(1):
      #(article_batch, _, _, article_lens, _, _, origin_articles,origin_abstracts) = self._batch_reader.NextBatch()
      #for i in xrange(self._hps.batch_size):
      #for i in xrange(1):

        #print "]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]"
        #print self._model
        #print self._hps.batch_size
        #print data.SENTENCE_START
        #print data.SENTENCE_END
        #print self._hps.dec_timesteps
        #print "]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]"

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

    #article_batch_cp = article_batch.copy()
    #print "row="+str(len(article_batch_cp))+"  col="+str(len(article_batch_cp[0]))
    w, h = 120, 4
    article_batch_cp = [[0 for x in range(w)] for y in range(h)] 
    print "row="+str(len(article_batch_cp))+"  col="+str(len(article_batch_cp[0]))
    #article_batch_cp = [[],[],[],[]]
    #print "111111"
    #print article_batch_cp
    #print "-------"
    #print self._hps.enc_timesteps
    #print article_sentences
    #print enc_inputs
    #print article_batch[i]
    #print article_batch[i:i+1]
    #print "-------"

    #article_batch_cp[:] = enc_inputs
    for i in range(0,4):
      article_batch_cp[i] = enc_inputs#article_batch[i]
    #article_batch_cp[:] = [enc_inputs for i in range(len(article_batch_cp)-4)]

    #print article_batch_cp
    #print "222222"
    #print article_batch_cp

    w, h = 1, 4
    article_lens_cp = [[0 for x in range(w)] for y in range(h)] 
    #article_lens_cp = article_lens.copy()
    for i in range(0,4):
      article_lens_cp[i] = enc_input_len
    #article_lens_cp[:] = enc_input_len #article_lens[i]
    

    #print "[[[[[[[[[[[[[[[[[[[[[[[[[[[["
    #print "--------->" + str(i) + "  len(article_batch)=" + str(len(article_batch))
    #print article_batch_cp
    #print article_lens_cp
    #print "[[[[[[[[[[[[[[[[[[[[[[[[[[[["
    #best_beam = bs.BeamSearch(sess, article_batch_cp, article_lens_cp)[0]
    best_beam = bs.BeamSearch(self._sess, article_batch_cp, article_lens_cp)
    print len(best_beam)
    best_beam = best_beam[0]
     
    decode_output = [int(t) for t in best_beam.tokens[1:]]

    #print "\\\\\\\\\\\\\\\\\\"
    #print origin_articles[i]
    #print origin_abstracts[i]
    #print decode_output
    QUESTION = article_text
    #print "<Question>"+article_text
    test = ' '.join(data.Ids2Words(decode_output, self._vocab))
    end_p = test.find(data.SENTENCE_END, 0)

    if end_p != -1:
      test = test[:end_p]
    #print "<Answer>"+test
    ANSWER = test.replace('<UNK>','')
    #print "\\\\\\\\\\\\\\\\\\"
        #self._DecodeBatch(origin_articles[i], origin_abstracts[i], decode_output)
    return QUESTION, ANSWER

  def _DecodeBatch(self, article, abstract, output_ids):
    """Convert id to words and writing results.
    Args:
      article: The original article string.
      abstract: The human (correct) abstract string.
      output_ids: The abstract word ids output by machine.
    """
    decoded_output = ' '.join(data.Ids2Words(output_ids, self._vocab))
    end_p = decoded_output.find(data.SENTENCE_END, 0)
    if end_p != -1:
      decoded_output = decoded_output[:end_p]
    tf.logging.info('article:  %s', article)
    tf.logging.info('abstract: %s', abstract)
    tf.logging.info('decoded:  %s', decoded_output)
    #print "!!!!!!!!!!!!!!!!!!!!!!!  decoded_output !!!!!!!!!!!!"
    #print decoded_output
    self._decode_io.Write(abstract, decoded_output.strip())
