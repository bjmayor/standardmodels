# note: this overrides the built-in 'repr' function
from repr import repr
# an annoyingly recursive data structure
data = (
"X" * 100000,
    )
data = [data]
data.append(data)
print repr(data)