import importlib
import os
from beelzebubb.core.exceptions import BeelzebuBBError

class PluginError(BeelzebuBBError):
    pass

class Plugins:
    
    def __init__(self):
        self.plugins = self.list_plugins()
        self.imported = []

    def list_plugins(self):
        root, dirs, _ = next(os.walk(os.path.join(os.getcwd(), 'beelzebubb', 'plugins')))
        plugins = []
        for d in dirs:
            if '__plugin__.py' not in os.listdir(os.path.join(root, d)): continue
            f = open(os.path.join(root, d, '__plugin__.py'), 'r')
            desc = eval(f.read())
            f.close()
            desc['name'] = d
            plugins.append(desc)
        return plugins
    
    def next(self):
        if len(self.plugins) == 0: return None
        found = False
        for p in self.plugins:
            ok = True
            for d in p['depends']:
                if d not in self.imported:
                    ok = False
                    break
            if ok:
                found = True 
                break
        if not found:
            raise PluginError('Couldn\'t resolve dependencies! Imported plugins: %s'
                                % (', '.join(self.imported) if self.imported else 'none'))
        self.plugins.remove(p)
        self.imported.append(p['name'])
        return p
        
def import_plugins():
    plugins = Plugins()
    
    print('Importing plugins...')
    p = plugins.next()
    while p:
        importlib.import_module('beelzebubb.plugins.' + p['name'])
        print('Imported ' + p['name'])
        p = plugins.next()
        
import_plugins()
    