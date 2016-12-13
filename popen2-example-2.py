import popen2
import string
class Chess:
    "Interface class for chesstool-compatible programs"
    def __init__(self, engine = "gnuchessc"):
        self.fin, self.fout = popen2.popen2(engine)
        s = self.fin.readline()
        if s != "Chess\n":
            raise IOError, "incompatible chess program"
    def move(self, move):
        self.fout.write(move + "\n")
        self.fout.flush()
        my = self.fin.readline()
        if my == "Illegal move":
            raise ValueError, "illegal move"
        his = self.fin.readline()
        return string.split(his)[2]
    def quit(self):
        self.fout.write("quit\n")
        self.fout.flush()
#
# play a few moves
g = Chess()
print g.move("a2a4")
print g.move("b2b3")
g.quit()
