from deviceState import deviceState
from inputHandler import *
from simCardInfo import *
from warehouseInfo import *
from inputHandler import *
from mockKeyInjection import *
from damageRating import *
from mockDatabaseRepo import *

class device:
    def __init__(self, serialNumber, boxNumber, crateNumber, damageRating, flashed, keyInjected, sendForRepacking, IMEI):
        self.serialNumber = serialNumber
        self.boxNumber = boxNumber
        self.crateNumber = crateNumber
        self.damageRating = damageRating
        self.flashed = flashed
        self.keyInjected = keyInjected
        self.sendForRepacking = sendForRepacking
        self.IMEI = IMEI
    
    def __init__(self, serialNumber, IMEI):
        self.serialNumber = serialNumber
        self.IMEI = IMEI
        self.state = deviceState.IMEI_RECORDED
    
    def setIMEI(self, IMEI):
        self.IMEI = IMEI
        self.state = deviceState.IMEI_RECORDED
    
    def returnIMEI(self):
        return self.IMEI
    
    def setSerialNumber(self, serialNumber):
        self.serialNumber = serialNumber
        self.state = deviceState.SERIAL_NUMBER_RECORDED
    
    def returnSerialNumber(self):
        return self.serialNumber
    
    def set_package_info(self, boxNumber, crateNumber):
        self.boxNumber = boxNumber
        self.crateNumber = crateNumber
        self._state = deviceState.STORED_IN_WAREHOUSE
    
    def setDamaged(self, damageRating):
        if self.damageRating > 0:
            self.setDeviceState("DAMAGE_RECORDED")
            self.flashed = None
            self.keyInjected = None
            self.sendForRepacking = None
            self.IMEI = None

    def returnFlashed(self):
        return self.flashed

    def returnKeyInjected(self):
        return self.keyInjected

    def returnSerialNumber(self):
        return self.serialNumber
    
    def getDeviceState(self):
        return self.deviceState

    def setDeviceState(self, state):
        self.deviceState = state

    def setSimCardInfo(self, SNN, IMSI):
        self.simcard = simCardInfo(SNN, IMSI)
        self.setDeviceState("SIM_INSERTED_AND_RECORDED")
    
    def setWarehouseInfo(self, warehouseNumber, sectionNumber, rowNumber, shelfNumber, segmentNumber, segment):
        self.warehouse = warehouseInfo(warehouseNumber, sectionNumber, rowNumber, shelfNumber, segmentNumber, segment)
        self.setDeviceState("STORED_IN_WAREHOUSE")
    
    def updateKeys(self, key):
        self.keyInjected = key
    
    def updateFlashed(self):
        self.flashed = True
    
    def modifyDevice(self):
        userDeviceIMEI = input("Please enter device IMEI: ")
        mockDB = mockDatabaseRepo()
        userDevice = mockDB.getDeviceByIMEI(userDeviceIMEI)
        print("Device is currently in {} state".format(userDevice.getDeviceState()))
    
    def startProgram():
        mockDB = mockDatabaseRepo()
        inputNewDevice = input("Would you like to register a new device? Y/N: ")
        if inputNewDevice == "Y":
            newDevice = device(input("Enter device serial number: "), input("Enter device box number: "), input("Enter damage from 1-5: "), input("Enter imsi number: "), input("Is device flashed (True/False): "), input("Is device key injected (True/False): "), input("Device needs to be repacked (True/False): "), input("Enter IMEI number: "))
            mockDB.appendToDeviceList(newDevice)
        else:
            userDeviceIMEI = input("Please enter device IMEI: ")
            userDevice = mockDB.getDeviceByIMEI(userDeviceIMEI)
            print(type(userDevice))
            print(userDevice.returnSerialNumber())

deviceDamageTest = device(123, 1, 2, 5, False, False, False, 8181)
deviceDamageTest.setDamaged()

deviceTest = device(123, 1, 2, 0, False, False, False, 8181)
deviceTest.setSimCardInfo(1,3)
deviceTest.setWarehouseInfo(1, 2, 3, 4, 5, 1)