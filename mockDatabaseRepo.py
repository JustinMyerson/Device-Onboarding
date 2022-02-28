from device import *
from inputHandler import *

class mockDatabaseRepo:
    def __init__(self):
        self.listOfDevices = []
    
    def getSizeOfListOfDevices(self):
        return len(self.listOfDevices)

    def appendToDeviceList(self, deviceToAdd):
        self.listOfDevices.append(deviceToAdd)
    
    def getDeviceBySerial(self, serialNumber):
        for device in self.listOfDevices:
            if device.returnSerialNumber() == serialNumber:
                return device

    def getDeviceByIMEI(self, IMEINumber):
        for device in self.listOfDevices:
            if device.returnIMEI() == IMEINumber:
                return device

    def checkIfFlashed(self, IMEINumber):
        for device in self.listOfDevices:
            if device.returnIMEI() == IMEINumber:
                if device.returnFlashed():
                    return True
                else:
                    return False
    
    def checkIfKeyInjected(self, IMEINumber):
        for device in self.listOfDevices:
            if device.returnIMEI() == IMEINumber:
                if device.returnKeyInjected():
                    return True
                else:
                    return False