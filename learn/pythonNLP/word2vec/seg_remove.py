# coding:utf-8

import logging
import os.path
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def seg_remove(input_path, output_path):
    output = open(output_path, 'w')
    input_file = open(input_path, 'r')

    for line in input_file.readlines():
        ss = re.findall('[\n\s*\r\u4e00-\u9fa5]', line)
        output.write("".join(ss))

if __name__ == '__main__':

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    stop_word_path = ''
    input_path = '../../data/wiki/wiki.cn.text.jian.seg'
    output_path = '../../data/wiki/wiki.cn.text.jian.remove'
    print time.time()
    seg_remove(input_path, output_path)
    print time.time()
