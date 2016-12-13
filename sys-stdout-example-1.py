# coding=UTF-8
import sys
import string
class Redirect:
    def __init__(self, stdout):
        self.stdout = stdout
    def write(self, s):
        self.stdout.write(string.lower(s))
# redirect standard output (including the print statement) # 重定向标准输出(包括 print 语句)
old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)
print "HEJA SVERIGE",
print "FRISKT HUM\303\226R"
# restore standard output # 恢复标准输出
sys.stdout = old_stdout
print "M\303\205\303\205\303\205\303\205L!"