import tokenize
file = open("tokenize-example-1.py")
def handle_token(type, token, (srow, scol), (erow, ecol), line):
    print "%d,%d-%d,%d:\t%s\t%s" % \
(srow, scol, erow, ecol, tokenize.tok_name[type], repr(token))
tokenize.tokenize(
    file.readline,
    handle_token
    )