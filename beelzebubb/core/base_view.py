from .base_meta import BaseMeta, Registry
from beelzebubb import app
from flask import request

ViewRegistry = Registry()

# This will handle dynamic inheritance of views, so that plugins
# will be able to overload them    
class ViewMeta(BaseMeta):
    reg = ViewRegistry
    what = 'view'
    base = 'BaseView'
    
    @classmethod
    def construct_new(cls, _name, name, bases, d):
        newcls = super().construct_new(_name, name, bases, d)
        cls.reg.unregister(_name)
        cls.reg.register(_name, newcls())

class BaseView(metaclass=ViewMeta):
    url = ''
    _name = ''
    
    def urls(self):
        return [{
                 'url': self.url,
                 'endpoint': self._name,
                 'view': lambda *args, **kwargs: self.view(request, *args, **kwargs),
                 }]
    
    def __init__(self):
        for url in self.urls():
            app.add_url_rule(url['url'], url['endpoint'], url['view'])
            
    def view(self, *args, **kwargs):
        raise NotImplementedError
    