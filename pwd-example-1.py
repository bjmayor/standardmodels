import pwd
import os
print pwd.getpwuid(os.getgid())
print pwd.getpwnam("root")