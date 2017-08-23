# coding:utf-8

import logging
import os.path
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def wiki_segment(stop_word_path, input_path, output_path):
    # jieba.analyse.set_stop_words(stop_word_path)
    output = open(output_path, 'w')
    input_file = open(input_path, 'r')
    space = ' '
    for line in input_file.readlines():
        seg_list = jieba.cut(line)
        output.write(space.join(seg_list) + '\n')


if __name__ == '__main__':

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    stop_word_path = ''
    input_path = '../../data/wiki/wiki.zh.text.jian'
    output_path = '../../data/wiki/wiki.cn.text.jian.seg'
    wiki_segment(stop_word_path, input_path, output_path)