import marshal
script = """
print 'hello'
"""
code = compile(script, "<script>", "exec")
data = marshal.dumps(code)
# intermediate format
print type(data), len(data)
print "-"*50
print repr(data)
print "-"*50
exec marshal.loads(data)