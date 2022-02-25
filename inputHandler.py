class inputHandler:
    def __init__(self):
        self.serialNumber = input("Enter device serial number: ")
        self.boxNumber = input("Enter device box number: ")
        self.crateNumber = input("Enter device crate number: ")
        self.damaged = input("Enter damage from 1-5: ")
        self.snn = input("Enter snn number: ")
        self.imsi = input("Enter imsi number: ")
        self.flashed = input("Is device flashed (True/False): ")
        self.keyInjected = input("Is device key injected (True/False): ")
        self.sendForRepacking = input("Device needs to be repacked (True/False): ")

    def returnInput(self):
        return self.serialNumber, self.boxNumber, self.crateNumber, self.damaged, self.snn, self.imsi, self.flashed, self.keyInjected, self.sendForRepacking
