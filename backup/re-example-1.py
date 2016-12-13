# coding=UTF-8
import re
text = "The Attila the Hun Show"
# a single character 单个字符
m = re.match(".", text)
if m: print repr("."), "=>", repr(m.group(0))
# any string of characters 任何字符串
m = re.match(".*", text)
if m: print repr(".*"), "=>", repr(m.group(0))
# a string of letters (at least one) 只包含字母的字符串(至少一个)
m = re.match("\w+", text)
if m: print repr("\w+"), "=>", repr(m.group(0))
# a string of digits 只包含数字的字符串
m = re.match("\d+", text)
if m: print repr("\d+"), "=>", repr(m.group(0))
