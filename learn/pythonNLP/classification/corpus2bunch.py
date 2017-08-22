# coding:utf-8
import sys
import os
import cPickle as pickle

reload(sys)
sys.setdefaultencoding('utf-8')

from sklearn.datasets.base import Bunch

def _readfile(path):
    with open(path, 'rb') as fp:
        content = fp.read()
    return content


def corpus2Bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)


    # target_name：是一个list，存放的是整个数据集的类别集合。
    # label：是一个list，存放的是所有文本的标签。
    # filenames：是一个list，存放的是所有文本文件的名字。
    # contents：是一个list，分词后文本文件词向量形式
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)

    for mydir in catelist:
        class_path = seg_path + mydir + '/'
        print class_path
        file_list = os.listdir(class_path)
        for file_path in file_list:
            fullname = class_path + file_path
            bunch.label.append(mydir)
            bunch.filenames.append(fullname)
            bunch.contents.append(_readfile(fullname))

    with open(wordbag_path, 'wb') as file_obj:
        pickle.dump(bunch, file_obj)

    print 'build text object end'

if __name__ == '__main__':
    wordbag_path = '../data/train_word_bag/train_set.dat'
    seg_path = '../data/train_corpus_seg/'
    corpus2Bunch(wordbag_path, seg_path)

    wordbag_path = '../data/test_word_bag/test_set.dat'
    seg_path = '../data/test_corpus_seg/'
    corpus2Bunch(wordbag_path, seg_path)
















