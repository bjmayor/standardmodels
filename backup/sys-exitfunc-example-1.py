# coding=utf-8
import sys
def exitfunc():
    print "world"
sys.exitfunc = exitfunc
print "hello"
sys.exit(1)
print "there" # never printed # 不会被 print
