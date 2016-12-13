import msvcrt
import time
print "press SPACE to enter the serial number"
while not msvcrt.kbhit() or msvcrt.getch() != " ":
    # do something else

print ".",
    time.sleep(0.1)
print
# clear the keyboard buffer # 清除键盘缓冲区
while msvcrt.kbhit():
    msvcrt.getch()
serial = raw_input("enter your serial number: ")
print "serial number is", serial