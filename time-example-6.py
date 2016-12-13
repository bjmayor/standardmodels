# coding=UTF-8
import time
# make sure we have a strptime function! # 确认有函数 strptime
from _strptime import _strptime
try:
    _strptime = _strptime
except AttributeError:
    from _strptime import _strptime
print _strptime("31 Nov 00", "%d %b %y")
print _strptime("1 Jan 70 1:30pm", "%d %b %y %I:%M%p")
