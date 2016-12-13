import unicodedata
for char in [u"A", u"-", u"1", u"\N{LATIN CAPITAL LETTER O WITH DIAERESIS}"]:
    print repr(char),
    print unicodedata.category(char),
    print repr(unicodedata.decomposition(char)),
    print unicodedata.decimal(char, None),
    print unicodedata.numeric(char, None)