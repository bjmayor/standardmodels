import sgmllib
import string

class FoundTitle(Exception):
    pass
class ExtractTitle(sgmllib.SGMLParser):
    def __init__(self, verbose=0):
        sgmllib.SGMLParser.__init__(self, verbose)
        self.title = self.data = None
    def handle_data(self, data):
        if self.data is not None:
            self.data.append(data)
    def start_title(self, attrs):
        self.data = []
    def end_title(self):
        self.title = string.join(self.data, "")
        raise FoundTitle # abort parsing!
def extract(file):
    # extract title from an HTML/SGML stream
    p = ExtractTitle()
    try:
        while 1:
            # read small chunks
            s = file.read(512)
            if not s:
                break
            p.feed(s)
        p.close()
    except FoundTitle:
        return p.title
    return None
#
# try it out
print "html", "=>", extract(open("samples/sample.htm"))
print "sgml", "=>", extract(open("samples/sample.sgm"))