class mockFlashDevice:
    def flashDevice(self) -> bool:
        pass

class keyInjector(mockFlashDevice):
    def flashDevice(self) -> bool:
        return super().flashDevice()
