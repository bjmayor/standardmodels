import Queue
import bisect
Empty = Queue.Empty
class PriorityQueue(Queue.Queue):
    "Thread-safe priority queue"
    def _put(self, item):
        # insert in order
        bisect.insort_left(self.queue, item)
#
# try it
queue = PriorityQueue(0)
# add items out of order
queue.put((20, "second"))
queue.put((10, "first"))
queue.put((30, "third"))
# print queue contents
try:
    while 1:
        print queue.get_nowait()
except Empty:
    pass
