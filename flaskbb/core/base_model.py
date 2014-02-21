from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from .base_meta import BaseMeta, Registry

ModelRegistry = Registry()

# This will handle dynamic inheritance, so that plugins
# will be able to overload models
class ModelMeta(DeclarativeMeta, BaseMeta):    
    reg = ModelRegistry
    what = 'model'
    base = 'BaseModel'

BaseModel = declarative_base(name='BaseModel', metaclass=ModelMeta)