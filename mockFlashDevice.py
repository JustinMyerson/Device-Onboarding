from device import *

class mockFlashDevice:
    def flashDevice(self) -> bool:
        return False

class keyInjector(mockFlashDevice):
    def __init__(self, device: device):
        self.device = device

    def flashDevice(self) -> bool:
        try:
            self.device.flashDevice()
        except:
            raise "Could not flash device"
