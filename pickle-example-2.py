import pickle
import math
value = (
    "this is a long string" * 100,
    [1.2345678, 2.3456789, 3.4567890] * 100
    )
# text mode
data = pickle.dumps(value)
print type(data), len(data), pickle.loads(data) == value
# binary mode
data = pickle.dumps(value, 1)
print type(data), len(data), pickle.loads(data) == value