import popen2, string
fin, fout = popen2.popen2("sort")
fout.write("foo\n")
fout.write("bar\n")
fout.close()
print fin.readline(),
print fin.readline(),
fin.close()
