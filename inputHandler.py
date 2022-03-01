from deviceState import *
from mockDatabaseRepo import *

class inputHandler:
    def __init__(self, serialNumber, boxNumber, crateNumber, damaged, IMEI, snn, imsi, flashed, keyInjected, sendForRepacking):
        self.serialNumber = serialNumber
        self.boxNumber = boxNumber
        self.crateNumber = crateNumber
        self.damaged = damaged
        self.IMEI = IMEI
        self.snn = snn
        self.imsi = imsi
        self.flashed = flashed
        self.keyInjected = keyInjected
        self.sendForRepacking = sendForRepacking
    
    def startProgram():
        mockDB = mockDatabaseRepo()
        inputNewDevice = input("Would you like to register a new device? Y/N: ")
        if inputNewDevice == "Y":
            newDevice = input("Enter device serial number: "), input("Enter device box number: "), input("Enter damage from 1-5: "), input("Enter snn number: "), input("Enter imsi number: "), input("Is device flashed (True/False): "), input("Is device key injected (True/False): "), input("Device needs to be repacked (True/False): "), input("Enter IMEI number: ")  
            mockDB.appendToDeviceList(newDevice)
        else:
            userDeviceIMEI = input("Please enter device IMEI: ")
            userDevice = mockDB.getDeviceByIMEI(userDeviceIMEI)
            ("Please choose device state to start with from the following options:")
            count = 0
            for d in deviceState:
                print("{} - {}".format(count, d.name))
                count += 1

    userInput = startProgram()

    def returnInput(self):
        if self.damaged > 0:
            return self.serialNumber, self.boxNumber, self.crateNumber, self.damaged, None, None, None, None
        else:
            return self.serialNumber, self.boxNumber, self.crateNumber, self.damaged, self.flashed, self.keyInjected, self.sendForRepacking, self.IMEI
        