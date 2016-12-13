import gc
# create a simple object that links to itself
class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
    def addchild(self, node):
        node.parent = self
        self.children.append(node)
    def __repr__(self):
        return "<Node %s at %x>" % (repr(self.name), id(self))
# set up a self-referencing structure
root = Node("monty")
root.addchild(Node("eric"))
root.addchild(Node("john"))
root.addchild(Node("michael"))
# remove our only reference
del root
print gc.collect(), "unreachable objects"
print gc.collect(), "unreachable objects"