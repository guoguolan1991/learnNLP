# coding:utf-8

import logging
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gensim.corpora import WikiCorpus


def wiki_process(raw_data_path, output_path):
    output = open(output_path, 'w')
    wiki = WikiCorpus(raw_data_path, lemmatize=False, dictionary={})
    space = ' '.encode()
    i = 0
    for text in wiki.get_texts():
        output.write(str(space.join(text)) + '\n')
        i = i + 1
        if i % 10000 == 0:
            logger.info('saved ' + str(i) + ' articles')

    output.close()
    logger.info('Finished saved ' + str(i) + ' articles')

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    raw_data_path = '../../data/wiki/zhwiki-latest-pages-articles.xml.bz2'
    output_path = '../../data/wiki/wiki.zh.text'
    wiki_process(raw_data_path, output_path)

