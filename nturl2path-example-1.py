import nturl2path
file = r"c:\my\little\pony"
print nturl2path.pathname2url(file)
print nturl2path.url2pathname(nturl2path.pathname2url(file))