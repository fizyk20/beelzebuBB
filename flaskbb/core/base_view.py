class ViewRegistry:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.pool = {}

# This will handle dynamic inheritance of views, so that plugins
# will be able to overload them    
class ViewMeta(type):
    
    def __new__(cls, name, bases, d):
        return super().__new__(cls, name, bases, d)

class BaseView(metaclass=ViewMeta):
    
    pass