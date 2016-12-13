import marshal
value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
    )
data = marshal.dumps(value)

# intermediate format
print type(data), len(data)
print "-"*50
print repr(data)
print "-"*50
print marshal.loads(data)