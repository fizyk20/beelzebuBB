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
        '''Functon generating a list of all plugins.
        A plugin is identified by containing the __plugin__.py file with plugin metadata.'''
        # generate the list of all subdirectories in the plugin directory
        root, dirs, _ = next(os.walk(os.path.join(os.getcwd(), 'beelzebubb', 'plugins')))
        plugins = []
        for d in dirs:
            # check if the subdirectory contains __plugins__.py
            if '__plugin__.py' not in os.listdir(os.path.join(root, d)): continue
            # if yes, read it and evaluate
            f = open(os.path.join(root, d, '__plugin__.py'), 'r')
            desc = eval(f.read())
            f.close()
            desc['name'] = d    # name of the plugin is the name of the directory
            plugins.append(desc)
        return plugins
    
    def next(self):
        '''Returns the next plugin for which all dependencies are satisfied.'''
        if len(self.plugins) == 0: return None
        found = False
        # look for a plugin with satisfied dependencies
        for p in self.plugins:
            ok = True   #assume it's ok
            for d in p['depends']:
                if d not in self.imported:
                    ok = False  # if a dependency isn't satisfied, then the plugin shouldn't be loaded
                    break
            if ok:  # if still ok after the whole loop, then all dependencies are loaded and the plugin is ready
                found = True 
                break
        if not found:
            # no plugins to be imported have satisfied dependencies - report error
            raise PluginError('Couldn\'t resolve dependencies! Imported plugins: %s'
                                % (', '.join(self.imported) if self.imported else 'none'))
        self.plugins.remove(p)  # remove from the "to be imported" list
        self.imported.append(p['name']) # ...and add to "imported" list
        return p    # return found plugin
        
def import_plugins():
    plugins = Plugins()
    
    print('Importing plugins...')
    p = plugins.next()  # find next plugin to be loaded
    while p:    # if we still have plugins
        importlib.import_module('beelzebubb.plugins.' + p['name']) # then load
        print('Imported ' + p['name'])  # log success
        p = plugins.next()  # and go to the next one
        
import_plugins()    # import all plugins when the "plugins" module is imported
    