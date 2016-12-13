import shelve
import gdbm
def gdbm_shelve(filename, flag="c"):
    return shelve.Shelf(gdbm.open(filename, flag))
db = gdbm_shelve("dbfile")