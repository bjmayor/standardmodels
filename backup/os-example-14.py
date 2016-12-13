# coding=UTF-8
import os
import time
pid = os.fork()
if pid:
    os._exit(0)
    # kill original
print "daemon started"
time.sleep(10)
print "daemon terminated"#这里不会打印,是因为父进程退出之后,子进程变成了孤儿进程,脱离了终端.