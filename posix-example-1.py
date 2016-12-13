import posix
for file in posix.listdir("."):
    print file, posix.stat(file)[6]
