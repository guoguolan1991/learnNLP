# coding:utf-8
from langconv import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print(sys.version)
print(sys.version_info)

# 转换繁体到简体
def zh_jian(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def jian_zh(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line

line_chs='<>123asdasd把中文字符串进行繁体和简体中文的转换'
line_cht='<>123asdasd把中文字符串進行繁體和簡體中文的轉換'

ret_chs = "%s\n" % zh_jian(line_cht)
ret_cht = "%s\n" % jian_zh(line_chs)

print("chs='%s'", ret_cht)
print("cht='%s'", ret_cht)
