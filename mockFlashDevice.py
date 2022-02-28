from device import *
from errors import *

class mockFlashDevice:
    def flashDevice(self) -> bool:
        pass

class keyInjector(mockFlashDevice):
    def __init__(self, device: device):
        self.device = device

    def flashDevice(self) -> bool:
        try:
            self.device.flashDevice()
        except:
            raise FlashFaliureException
