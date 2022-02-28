from device import *

class mockKeyInjection:
    def __init__(self, key):
        self.key = key

    def injectKey(self, key) -> bool:
        return False

class keyInjector(mockKeyInjection):
    def __init__(self, device: device):
        self.device = device

    def injectKey(self, key: list) -> bool:
        try:
            self.device.injectKey(key)
        except:
            raise "Key not injected correctly"

