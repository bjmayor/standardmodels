import xmllib
class Parser(xmllib.XMLParser):
    # get quotation number
    def __init__(self, file=None):
        xmllib.XMLParser.__init__(self)
        if file:
            self.load(file)
    def load(self, file):
        while 1:
            s = file.read(512)
            if not s:
                break
            self.feed(s)
        self.close()
    def start_quotation(self, attrs):
        print "id =>", attrs.get("id")
        raise EOFError
try:
    c = Parser()
    c.load(open("samples/sample.xml"))
except EOFError:
    pass