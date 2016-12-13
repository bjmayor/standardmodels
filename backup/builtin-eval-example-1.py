def dump(expression):
    result = eval(expression)
    print expression, "=>", result, type(result)
dump("1")
dump("1.0")
dump("'string'")
dump("1.0 + 2.0")
dump("'*' * 10")
dump("len('world')")