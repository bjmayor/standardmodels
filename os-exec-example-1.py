import os
import sys
program = "python"
arguments = ["hello.py"]
print os.execvp(program, (program,) +  tuple(arguments))
print "goodbye"