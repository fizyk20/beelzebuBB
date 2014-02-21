from .base_meta import BaseMeta, Registry

ViewRegistry = Registry()

# This will handle dynamic inheritance of views, so that plugins
# will be able to overload them    
class ViewMeta(BaseMeta):
    reg = ViewRegistry
    what = 'view'

class BaseView(metaclass=ViewMeta):
    pass