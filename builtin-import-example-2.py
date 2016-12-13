def getfunctionbyname(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)

print(repr(getfunctionbyname("dumbdbm","open")))