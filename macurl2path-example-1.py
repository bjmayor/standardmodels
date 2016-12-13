import macurl2path
file = ":my:little:pony"
print macurl2path.pathname2url(file)
print macurl2path.url2pathname(macurl2path.pathname2url(file))