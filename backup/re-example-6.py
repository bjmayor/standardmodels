import re, string
def combined_pattern(patterns):
    p = re.compile(
        string.join(map(lambda x: "("+x+")", patterns), "|")
        )
    def fixup(v, m=p.match, r=range(0,len(patterns))):
        try:
            regs = m(v).regs
        except AttributeError:
            return None # no match, so m.regs will fail
        else:
            for i in r:
                if regs[i+1] != (-1, -1):
                    return i
    return fixup
#
# try it out!
patterns = [
    r"\d+",
    r"abc\d{2,4}",
r"p\w+" ]
p = combined_pattern(patterns)
print p("129391")
print p("abc800")
print p("abc1600")
print p("python")
print p("perl")
print p("tcl")