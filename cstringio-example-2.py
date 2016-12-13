try:
    import cStringIO
    StringIO = cStringIO
except ImportError:
    import StringIO
print StringIO