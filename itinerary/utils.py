
def cached_property(func):
    def _cached_property(*args, **kwargs):
        cls = args[0]
        cached_name = '_cached_' + func.__name__
        if not hasattr(cls, cached_name):
            val = func(*args, **kwargs)
            setattr(cls, cached_name, val)
        return getattr(cls, cached_name)
    return _cached_property

