import pickle
CODE = """
print 'good evening'
"""
code = compile(CODE, "<string>", "exec")
exec code
exec pickle.loads(pickle.dumps(code))