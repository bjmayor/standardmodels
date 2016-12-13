# coding=UTF-8
import sys
def test(n):
    j= 0
    for i in range(n):
        j=j+ i
    return n
def tracer(frame, event, arg):
    print event, frame.f_code.co_name, frame.f_lineno, "->", arg
    return tracer
# tracer is activated on the next call, return, or exception # 跟踪器将在下次函数调用, 返回, 或异常时激活
sys.settrace(tracer)
# trace this function call # 跟踪这次函数调用
test(1)
# disable tracing # 禁用跟踪器
sys.settrace(None)
# don't trace this call # 不会跟踪这次函数调用
test(2)