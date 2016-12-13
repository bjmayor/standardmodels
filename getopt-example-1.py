# coding=UTF-8
import getopt
import sys
# simulate command-line invocation
# 模仿命令行参数
sys.argv = ["myscript.py", "-l", "-d", "directory", "filename"]
# process options
# 处理选项
opts, args = getopt.getopt(sys.argv[1:], "ld:")
long = 0
directory = None

for o, v in opts:
    if o == "-l":
        long = 1
    elif o == "-d":
        directory = v
print "long", "=", long
print "directory", "=", directory
print "arguments", "=", args
