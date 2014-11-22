from beelzebubb.core.exceptions import BeelzebuBBError

class RegistryError(BeelzebuBBError):
    pass

# Registry class

class Registry:
    '''Generic registry for objects
    Together with appropriate metaclasses this allows to keep a list of all created classes.
    The user-defined class should inherit after a class exposed by the API - since its metaclass
    is associated with a registry, it will be registered and kept for later use.'''
    
    def __init__(self):
        self.pool = {}
        
    def register(self, name, obj):
        self.pool[name] = obj
        
    def unregister(self, name):
        del self.pool[name]
        
    def exists(self, name):
        return (name in self.pool)
        
    def get(self, name):
        if name not in self.pool:
            return None
        return self.pool[name]
    
    
# Basic metaclass for use with registries

class BaseMeta(type):
    '''The base for metaclasses interacting with registries.
    Generating a metaclass involves inheriting from BaseMeta and defining 3 parameters:
    * reg - the associated Registry subclass
    * what - the friendly name of object class served by this metaclass (Model / View / ...)
    * base - the name of the base class (since it usually shouldn't get written to the registry)'''
    
    reg = None
    what = 'class'
    base = None
    
    def __new__(cls, name, bases, d):
        if name == cls.base:
            return super().__new__(cls, name, bases, d)
        if '_name' not in d and '_inherit' not in d:
            raise RegistryError('_name not defined in class %s' % name)
        _name = d['_name'] if '_name' in d else d['_inherit']
        _inherit = d['_inherit'] if '_inherit' in d else None
        if cls.reg.exists(_name):
            return cls.construct_inherited(_name, _inherit, name, bases, d)
        else:
            return cls.construct_new(_name, name, bases, d)
    
    @classmethod
    def construct_new(cls, _name, name, bases, d):
        newcls = super().__new__(cls, name, bases, d)
        cls.reg.register(_name, cls)
        return newcls
    
    @classmethod
    def construct_inherited(cls, _name, _inherit, name, bases, d):
        if not _inherit:
            raise RegistryError('%s named %s already exists and is not being inherited by class %s!' % (cls.what.capitalize(), _name, name))
        newcls = cls.reg.get(_name) # TODO - implement inheritance
        return newcls
    