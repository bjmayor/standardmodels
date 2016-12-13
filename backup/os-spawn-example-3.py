import os
import string
if os.name in ("nt", "dos"):
    exefile = ".exe"
else:
    exefile = ""
def spawn(program, *args):
    try:
        # possible 2.0 shortcut!
        return os.spawnvp(os.P_WAIT ,program, (program,) + args)
    except AttributeError:
        pass
    try:
        spawnv = os.spawnv
    except AttributeError: # assume it's unix
        pid = os.fork()
        if not pid:
            os.execvp(program, (program,) + args)
            return os.wait()[0]
        else: # got spawnv but no spawnp: go look for  an executable
            for path in string.split(os.environ["PATH"], os.pathsep):
                file = os.path.join(path, program) + exefile
                try:
                    return spawnv(os.P_WAIT, file, (file,) + args)
                except os.error:
                    pass
                    raise IOError, "cannot find executable" # # try it out!
spawn("python", "hello.py")
print "goodbye"
