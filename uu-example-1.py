import uu
import os, sys
infile = "samples/sample.png"
uu.encode(infile, sys.stdout, os.path.basename(infile))
