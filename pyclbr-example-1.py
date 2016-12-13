import pyclbr
mod = pyclbr.readmodule("cgi")
for k, v in mod.items():
    print k, v