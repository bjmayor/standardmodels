import ihooks, imp, os

def import_from(filename):
    "Import module from a named file"
    loader = ihooks.BasicModuleLoader()
    path, file = os.path.split(filename)
    name, ext  = os.path.splitext(file)
    m = loader.find_module_in_dir(name, path)
    if not m:
        raise ImportError, name
    m = loader.load_module(name, m)
    return m
colorsys = import_from("/python/lib/colorsys.py")
print colorsys