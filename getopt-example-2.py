#coding=UTF-8
import getopt
import sys
# simulate command-line invocation
# 模仿命令行参数
sys.argv = ["myscript.py", "--echo", "--printer", "lp01", "message"]
opts, args = getopt.getopt(sys.argv[1:], "ep:", ["echo", "printer="])
# process options # 处理选项
echo = 0
printer = None
for o, v in opts:
    if o in ("-e", "--echo"):
        echo = 1
    elif o in ("-p", "--printer"):
        printer = v
print "echo", "=", echo
print "printer", "=", printer
print "arguments", "=", args
