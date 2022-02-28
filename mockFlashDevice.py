from device import *
from errors import *

class mockFlashDevice:
    def flashDevice(self):
        pass

class flashDevice(mockFlashDevice):
    def __init__(self, device):
        self._device = device

    def flashDevice(self):
        try:
            device.flashed = True
        except:
            raise FlashFaliureException
