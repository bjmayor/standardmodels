# coding=UTF-8
class Rectangle:
    def __init__(self, color="white", width=10, height=10):
        print ("create a", color, self, "sized ", width,"x", height)


class RoundedRectangle(Rectangle):
    def __init__(self, **kw):
        #直接调用是Rectangle.__init__(self,**kw)
        apply(Rectangle.__init__, (self,), kw)

rect = Rectangle(color="green", height=100, width=100)
rect = RoundedRectangle(color="blue", height=20)

