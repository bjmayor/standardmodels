import sndhdr
result = sndhdr.what("samples/sample.wav")
if result:
    print "file format:", result
else:
    print "cannot identify file"