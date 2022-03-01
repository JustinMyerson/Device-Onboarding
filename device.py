from deviceState import deviceState
from inputHandler import *
from simCardInfo import *
from warehouseInfo import *
from inputHandler import *
from mockKeyInjection import *
from damageRating import *

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
    
    def returnIMEI(self):
        return self.IMEI
    
    def setDamaged(self):
        if self.damageRating > 0:
            self.setDeviceState("DAMAGE_RECORDED")
            self.flashed = None
            self.keyInjected = None
            self.sendForRepacking = None
            self.IMEI = None
            print("Device is damaged and will not be usable")

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

deviceDamageTest = device(123, 1, 2, 5, False, False, False, 8181)
deviceDamageTest.setDamaged()

deviceTest = device(123, 1, 2, 0, False, False, False, 8181)
deviceTest.setSimCardInfo(1,3)
deviceTest.setWarehouseInfo(1, 2, 3, 4, 5, 1)