import thread
import time, random

def worker():
    for i in range(50):
        # pretend we're doing something that takes 10?00 ms
        time.sleep(random.randint(10, 100) / 1000.0)
        print thread.get_ident(), "-- task", i, "finished"
#
# try it out!
for i in range(2):
    thread.start_new_thread(worker, ())
time.sleep(1)
print "goodbye!"