# coding=UTF-8
import sys
def test(n):
    j= 0
    for i in range(n):
        j=j+ i
    return n

def profiler(frame, event, arg):
    print event, frame.f_code.co_name, frame.f_lineno, "->", arg
# profiler is activated on the next call, return, or exception # 分析函数将在下次函数调用, 返回, 或异常时激活
sys.setprofile(profiler)
# profile this function call # 分析这次函数调用
test(1)
# disable profiler
# 禁用分析函数
sys.setprofile(None)
# don't profile this call # 不会分析这次函数调用
test(2)