# coding:utf-8
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')


def savefile(filepath, content):
    with open(filepath, 'wb') as fp:
        fp.write(content)


def readfile(path):
    with open(path, 'rb') as fp:
        content = fp.read()
    return content


def corpus_segment(corpus_path, seg_path):
    '''
    语料分词
    :param corpus_path: 未分词语料库路径
    :param seg_path: 分词后语料库路径
    :return: 
    '''
    catelist = os.listdir(corpus_path)

    for mydir in catelist:
        class_path = corpus_path + mydir + '/'
        seg_dir = seg_path + mydir + '/'

        if not os.path.exists(seg_dir):
            os.makedirs(seg_dir)

        file_list = os.listdir(class_path)

        for file_path in file_list:
            fullname = class_path + file_path
            content = readfile(fullname)
            '''
            此时，content里面存贮的是原文本的所有字符，例如多余的空格、空行、回车等等， 
            接下来，我们需要把这些无关痛痒的字符统统去掉，变成只有标点符号做间隔的紧凑的文本内容 
            '''
            content = content.replace('\r\n', '').replace(' ', '')
            content_seg = jieba.cut(content)
            savefile(seg_dir + file_path, ' '.join(content_seg))

    print('segment end!')


if __name__ == '__main__':
    corpus_path = './data/train_corpus'
    seg_path = './data/train_corpus_seg'
    corpus_segment(corpus_path, seg_path)

    # corpus_path = './data/test_corpus'
    # seg_path = './data/test_corpus_seg'
    # corpus_segment(corpus_path, seg_path)






































