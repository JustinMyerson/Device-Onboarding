from device import *
from errors import *

class mockKeyInjection:
    def injectKey(self):
        pass

class keyInjector(mockKeyInjection):
    def __init__(self, key):
        self.key = key

    def injectKey(self, device):
        try:
            self.device.injectKey(985241)
            return True
        except:
            raise InjectionFaliureException

