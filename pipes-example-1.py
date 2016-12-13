#coding=UTF-8
import pipes
t = pipes.Template()
# create a pipeline
# 这里 " - " 代表从标准输入读入内容
t.append("sort", "--")
t.append("uniq", "--")
# filter some text
# 这里空字符串代表标准输出
t.copy("samples/sample.txt", "")
