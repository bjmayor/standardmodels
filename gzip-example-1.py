import gzip
file = gzip.GzipFile("samples/sample.gz")
print file.read()