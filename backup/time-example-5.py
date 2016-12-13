import time
def procedure():
    time.sleep(2.5)
# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"
# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"
