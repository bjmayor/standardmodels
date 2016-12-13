import filecmp
if filecmp.cmp("samples/book.txt", "samples/other.txt"):
    print "files are identical"
else:
    print "files differ!"