import sys
print "path has", len(sys.path), "members"
# add the sample directory to the path
sys.path.insert(0, "samples")
import sample
# nuke the path
sys.path = []
import random # oops!