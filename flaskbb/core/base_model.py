from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModelRegistry:
    _instance = None
    
    # make the registry a singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            return super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.pool = {}

# This will handle dynamic inheritance, so that plugins
# will be able to overload models
class ModelMeta(Base.__class__):
    
    def __new__(cls, name, bases, d):
        return super().__new__(cls, name, bases, d)

class BaseModel(Base, metaclass=ModelMeta):
    pass