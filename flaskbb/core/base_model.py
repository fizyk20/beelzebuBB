from sqlalchemy.ext.declarative import declarative_base
from .base_meta import BaseMeta, Registry

Base = declarative_base()

ModelRegistry = Registry()

# This will handle dynamic inheritance, so that plugins
# will be able to overload models
class ModelMeta(Base.__class__, BaseMeta):    
    reg = ModelRegistry
    what = 'model'

class BaseModel(Base, metaclass=ModelMeta):
    pass