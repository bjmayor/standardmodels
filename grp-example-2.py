import grp
import os
# preload password dictionary
_grp = {}
for info in grp.getgrall():
    _grp[info[0]] = _grp[info[2]] = info
def groupinfo(gid):
    # name or gid integer
    return _grp[gid]
print groupinfo(os.getgid())
print groupinfo("wheel")