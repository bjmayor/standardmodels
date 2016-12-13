# coding=UTF-8
import re
text = "you're no fun anymore..."
# literal replace (string.replace is faster) # 文字替换 (string.replace 速度更快)
print re.sub("fun", "entertaining", text)
# collapse all non-letter sequences to a single dash # 将所有非字母序列转换为一个"-"(dansh,破折号)
print re.sub("[^\w]+", "-", text)
# convert all words to beeps
# 将所有单词替换为 BEEP
print re.sub("\S+", "-BEEP-", text)