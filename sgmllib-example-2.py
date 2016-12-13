import sgmllib
import cgi, sys
class PrettyPrinter(sgmllib.SGMLParser):
    # A simple SGML pretty printer
    def __init__(self):
        # initialize base class
        sgmllib.SGMLParser.__init__(self)
        self.flag = 0
    def newline(self):
        # force newline, if necessary
        if self.flag:
            sys.stdout.write("\n")
        self.flag = 0
    def unknown_starttag(self, tag, attrs):
        # called for each start tag
        # the attrs argument is a list of (attr, value)
        # tuples. convert it to a string.
        text = ""
        for attr, value in attrs:
            text = text + " %s='%s'" % (attr, cgi.escape(value))
        self.newline()
        sys.stdout.write("<%s%s>\n" % (tag, text))
    def handle_data(self, text):
        # called for each text section
        sys.stdout.write(text)
        self.flag = (text[-1:] != "\n")
    def handle_entityref(self, text):
        # called for each entity
        sys.stdout.write("&%s;" % text)
    def unknown_endtag(self, tag):
        # called for each end tag
        self.newline()
        sys.stdout.write("<%s>" % tag)
#
# try it out
file = open("samples/sample.sgm")
p = PrettyPrinter()
p.feed(file.read())
p.close()
