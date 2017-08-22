# coding:utf-8
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

import cPickle as pickle
from sklearn.naive_bayes import MultinomialNB

def _readbuchObj(path):
    with open(path, 'rb') as fp:
        bunch = pickle.load(fp)
    return bunch

trainpath = '../data/train_word_bag/tfidfspace.dat'
train_set = _readbuchObj(trainpath)

testpath = '../data/test_word_bag/testspace.dat'
test_set = _readbuchObj(testpath)

clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

predicted = clf.predict(test_set.tdm)

for flabel, file_name, expct_cate in zip(test_set.label, test_set.filenames, predicted):
    if flabel != expct_cate:
        print file_name, ": 实际类别：", flabel, "-->预测类别：", expct_cate

print 'predict end'

from sklearn import metrics


def metrics_result(actual, predict):
    print '精度:{0:.3f}'.format(metrics.precision_score(actual, predict, average='weighted'))
    print '召回:{0:0.3f}'.format(metrics.recall_score(actual, predict, average='weighted'))
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict, average='weighted'))

metrics_result(test_set.label, predicted)
