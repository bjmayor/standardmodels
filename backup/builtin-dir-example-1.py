def dump(value):
    print value, "=>", dir(value)

import sys
dump(0)
dump(1.0)
dump(0.0j)
dump([])
dump({})
dump("string")
dump(len)
dump(sys)