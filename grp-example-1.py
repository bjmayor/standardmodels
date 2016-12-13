import grp
import os
print grp.getgrgid(os.getgid())
print grp.getgrnam("wheel")