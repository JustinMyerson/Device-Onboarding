class mockFlashDevice:
    def flashDevice(self) -> bool:
        return False

class keyInjector(mockFlashDevice):
    def flashDevice(self) -> bool:
        return super().flashDevice()
