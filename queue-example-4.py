import Queue
Empty = Queue.Empty
class Stack(Queue.Queue):
    "Thread-safe stack"
    def _put(self, item):
        # insert at the beginning of queue, not at the end
        self.queue.appendleft(item)
    # method aliases
    push = Queue.Queue.put
    pop = Queue.Queue.get
    pop_nowait = Queue.Queue.get_nowait
#
# try it
stack = Stack(0)
# push items on stack
stack.push("first")
stack.push("second")
stack.push("third")
# print stack contents
try:
    while 1:
        print stack.pop_nowait()
except Empty:
    pass