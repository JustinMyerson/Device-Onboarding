from device import Device
from inputHandler import *

class mockDatabaseRepo:
    def __init__(self):
        self.listOfDevices = []
    
    def getSizeOfListOfDevices(self):
        return len(self.listOfDevices)
    
    def create_device(self, serialNumber, IMEI):
        self.listOfDevices.append(Device(serialNumber, IMEI))

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
        dev = self.getDeviceByIMEI(IMEINumber)
        if dev.returnFlashed():
            return True
        return False
    
    def checkIfKeyInjected(self, IMEINumber):
        dev = self.getDeviceByIMEI(IMEINumber)
        if dev.returnKeyInjected():
            return True
        return False