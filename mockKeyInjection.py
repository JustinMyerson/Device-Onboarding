from device import *
from errors import *

class mockKeyInjection:
    def injectKey(self):
        pass

class keyInjector(mockKeyInjection):
    def __init__(self, device):
        self.device = device

    def injectKey(self, key):
        try:
            self.device.injectKey(key)
            return True
        except:
            raise InjectionFaliureException

