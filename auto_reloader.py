from types import ModuleType
from importlib import reload

class AutoReloader:
    def __init__(self, module):
        self.module = module

    def _deep_reload(self, module):
        reload(module)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if type(attribute) is ModuleType:
                self._deep_reload(attribute)

    def __getattr__(self, name):
        self._deep_reload(self.module)
        return getattr(self.module, name)
