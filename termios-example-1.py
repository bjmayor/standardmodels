import termios
import sys
fileno = sys.stdin.fileno()
attr = termios.tcgetattr(fileno)
orig = attr[:]
print "attr =>", attr[:4] # flags
# disable echo flag
attr[3] = attr[3] & ~termios.ECHO
try:
    termios.tcsetattr(fileno, termios.TCSADRAIN, attr)
    message = raw_input("enter secret message: ")
    print
finally:
    # restore terminal settings
    termios.tcsetattr(fileno, termios.TCSADRAIN, orig)
print "secret =>", repr(message)