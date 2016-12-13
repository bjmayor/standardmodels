import locale
print "locale", "=>", locale.setlocale(locale.LC_ALL, "")
# integer formatting
value = 4711
print locale.format("%d", value, 1), "==",
print locale.atoi(locale.format("%d", value, 1))
# floating point
value = 47.11
print locale.format("%f", value, 1), "==",
print locale.atof(locale.format("%f", value, 1))
info = locale.localeconv()
print info["int_curr_symbol"]