# coding:utf-8

import logging
import multiprocessing
import os.path
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def train_word2vec_model(raw_data_path, model_path, vector_path):
    model = Word2Vec(LineSentence(raw_data_path), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(model_path)
    model.wv.save_word2vec_format(vector_path, binary=False)

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    # check and process input arguments
    raw_data_path = '../../data/wiki/wiki.cn.text.jian.seg'
    model_path = '../../data/wiki/wiki.cn.text.jian.model'
    vector_path = '../../data/wiki/wiki.cn.text.jian.vector'

    time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    train_word2vec_model(raw_data_path, model_path, vector_path)
    time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

