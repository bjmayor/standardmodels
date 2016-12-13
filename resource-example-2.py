import resource
resource.setrlimit(resource.RLIMIT_CPU, (0, 1))
# pretend we're busy
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            pass