from flask.ext.sqlalchemy import SQLAlchemy as OldSQLAlchemy, _BoundDeclarativeMeta, Model, _QueryProperty
from sqlalchemy.ext.declarative import declarative_base
from ..base_meta import BaseMeta, Registry

ModelRegistry = Registry()

class ModelMeta(_BoundDeclarativeMeta, BaseMeta):    
    reg = ModelRegistry
    what = 'model'
    base = 'Model'

class SQLAlchemy(OldSQLAlchemy):
    """Modified SQLAlchemy class - to register models in the registry"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def make_declarative_base(self):
        """Creates the declarative base."""
        base = declarative_base(cls=Model, name='Model',
                                metaclass=ModelMeta)
        base.query = _QueryProperty(self)
        return base