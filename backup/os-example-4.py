import os
# where are we?
cwd = os.getcwd()
print "1", cwd
# go down
os.chdir("samples")
print "2", os.getcwd()
# go back up
os.chdir(os.pardir)
print "3", os.getcwd()