import parser
import symbol, token
def dump_and_modify(node):
    name = symbol.sym_name.get(node[0])
    if name is None:
        name = token.tok_name.get(node[0])
    print name,
    for i in range(1, len(node)):
        item = node[i]
        if type(item) is type([]):
            dump_and_modify(item)
        else:
            print repr(item)
            if name == "NUMBER":
                # increment all numbers!
                node[i] = repr(int(item)+1)
ast = parser.expr("1 + 3")
list = ast.tolist()
dump_and_modify(list)
ast = parser.sequence2ast(list)
print eval(parser.compileast(ast))