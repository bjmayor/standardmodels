import urlparse
base = "http://spam.egg/my/little/pony"
for path in "/index", "goldfish", "../black/cat":
    print path, "=>", urlparse.urljoin(base, path)