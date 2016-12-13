import tty
import os, sys
fileno = sys.stdin.fileno()
tty.setraw(fileno)
print raw_input("raw input: ")
tty.setcbreak(fileno)
print raw_input("cbreak input: ")
os.system("stty sane") # ...