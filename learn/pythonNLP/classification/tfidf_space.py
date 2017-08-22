# coding:utf-8
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

from sklearn.datasets.base import Bunch
import cPickle as pickle

from sklearn.feature_extraction.text import TfidfVectorizer

def _readfile(path):
    with open(path, 'rb') as fp:
        content = fp.read()
    return content


def _readbuchObj(path):
    with open(path, 'rb') as fp:
        bunch = pickle.load(fp)
    return bunch


def _writebuchObj(path, bunchObj):
    with open(path, 'wb') as fp:
        pickle.dump(bunchObj, fp)


# 创建TF-IDF词向量空间
def vector_space(stopword_path, bunch_path, space_path, train_tfidf_path=None):
    '''
    关于参数，你只需要了解这么几个就可以了：
    stop_words:
    传入停用词，以后我们获得vocabulary_的时候，就会根据文本信息去掉停用词得到
    vocabulary:
    之前说过，不再解释。
    sublinear_tf:
    计算tf值采用亚线性策略。比如，我们以前算tf是词频，现在用1+log(tf)来充当词频。
    smooth_idf:
    计算idf的时候log(分子/分母)分母有可能是0，smooth_idf会采用log(分子/(1+分母))的方式解决。默认已经开启，无需关心。
    norm:
    归一化，我们计算TF-IDF的时候，是用TF*IDF，TF可以是归一化的，也可以是没有归一化的，一般都是采用归一化的方法，默认开启.
    max_df:
    有些词，他们的文档频率太高了（一个词如果每篇文档都出现，那还有必要用它来区分文本类别吗？当然不用了呀），所以，我们可以
    设定一个阈值，比如float类型0.5（取值范围[0.0,1.0]）,表示这个词如果在整个数据集中超过50%的文本都出现了，那么我们也把它列
    为临时停用词。当然你也可以设定为int型，例如max_df=10,表示这个词如果在整个数据集中超过10的文本都出现了，那么我们也把它列
    为临时停用词。
    min_df:
    与max_df相反，虽然文档频率越低，似乎越能区分文本，可是如果太低，例如10000篇文本中只有1篇文本出现过这个词，仅仅因为这1篇
    文本，就增加了词向量空间的维度，太不划算。
    当然，max_df和min_df在给定vocabulary参数时，就失效了。
    :param stopword_path: 
    :param bunch_path: 
    :param space_path: 
    :return: 
    '''
    stopword_list = _readfile(stopword_path).splitlines()
    bunch = _readbuchObj(bunch_path)

    # 构建tf-idf词向量空间对象
    tfidf_space = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[], vocabulary={})

    if train_tfidf_path is not None:
        trainbunch = _readbuchObj(train_tfidf_path)
        tfidf_space.vocabulary = trainbunch.vocabulary
        vectorizer = TfidfVectorizer(stop_words=stopword_list, sublinear_tf=True, max_df=0.5, vocabulary=trainbunch.vocabulary)
        tfidf_space.tdm = vectorizer.fit_transform(bunch.contents)
    else:
        vectorizer = TfidfVectorizer(stop_words=stopword_list, sublinear_tf=True, max_df=0.5)
        tfidf_space.tdm = vectorizer.fit_transform(bunch.contents)
        tfidf_space.vocabulary = vectorizer.vocabulary_

    _writebuchObj(space_path, tfidf_space)
    print 'tf-idf word vector build success'

if __name__ == '__main__':
    stopword_path = '../data/train_word_bag/stop_words.txt'
    bunch_path = '../data/train_word_bag/train_set.dat'
    space_path = '../data/train_word_bag/tfidfspace.dat'
    vector_space(stopword_path, bunch_path, space_path)

    bunch_path = "../data/test_word_bag/test_set.dat"
    space_path = "../data/test_word_bag/testspace.dat"
    # train_tfidf_path = "../data/train_word_bag/testspace.dat"
    vector_space(stopword_path, bunch_path, space_path)
















