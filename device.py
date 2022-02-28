from deviceState import deviceState
from inputHandler import *
from simCardInfo import *
from warehouseInfo import *
from inputHandler import *

class device:
    def __init__(self, serialNumber, boxNumber, crateNumber, isDamaged, flashed, keyInjected, sendForRepacking, IMEI):
        self.serialNumber = serialNumber
        self.boxNumber = boxNumber
        self.crateNumber = crateNumber
        self.isDamaged = isDamaged
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
    
    def setSimCardInfo(self, SNN, IMSI):
        self.simcard = simCardInfo(SNN, IMSI)
        self.setDeviceState("SIM_INSERTED_AND_RECORDED")
    
    def setWarehouseInfo(self, warehouseNumber, sectionNumber, rowNumber, shelfNumber, segmentNumber, segment):
        self.warehouse = warehouseInfo(warehouseNumber, sectionNumber, rowNumber, shelfNumber, segmentNumber, segment)
        self.setDeviceState("STORED_IN_WAREHOUSE")

deviceTest = device(123, 1, 2, False, False, False, False, 8181)
deviceTest.setSimCardInfo(1,3)
deviceTest.setWarehouseInfo(1, 2, 3, 4, 5, 1)

