# coding:utf-8
import sys
from lxml import html

reload(sys)
sys.setdefaultencoding('utf-8')

def html2txt(path):
    with open(path, 'rb') as f:
        content = f.read()

    page = html.document_fromstring(content)
    text = page.text_content()
    return text

if __name__ == '__main__':
    path = 'data/html/1.htm'
    text = html2txt(path)
    print text

