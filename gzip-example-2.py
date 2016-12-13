import gzip
class gzipFile(gzip.GzipFile):
    # adds seek/tell support to GzipFile
    offset = 0
    def read(self, size=None):
        data = gzip.GzipFile.read(self, size)
        self.offset = self.offset + len(data)
        return data
    def seek(self, offset, whence=0):
        # figure out new position (we can only seek forwards)
        if whence == 0:
            position = offset
        elif whence == 1:
            position = self.offset + offset
        else:
            raise IOError, "Illegal argument"
        if position < self.offset:
            raise IOError, "Cannot seek backwards"
        # skip forward, in 16k blocks
        while position > self.offset:
            if not self.read(min(position - self.offset, 16384)):
                break
    def tell(self):
        return self.offset
#
# try it
file = gzipFile("samples/sample.gz")
file.seek(80)
print file.read()