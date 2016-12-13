import pwd
import os
# preload password dictionary
_pwd = {}
for info in pwd.getpwall():
    _pwd[info[0]] = _pwd[info[2]] = info
def userinfo(uid):
    # name or uid integer
    return _pwd[uid]
print userinfo(os.getuid())
print userinfo("root")
