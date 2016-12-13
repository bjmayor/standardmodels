import re
text = "Example 3: There is 1 date 10/25/95 in here!"
m = re.search("(\d{1,2})/(\d{1,2})/(\d{2,4})", text)
print m.group(1), m.group(2), m.group(3)
month, day, year = m.group(1, 2, 3)
print month, day, year
date = m.group(0)
print date