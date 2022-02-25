from simCardInfo import *
from warehouseInfo import *

class device:
    def __init__(self, serialNumber, boxNumber, crateNumber, isDamaged, flashed, keyInjected, sendForRepacking, IMEI, deviceState):
        self.serialNumber = serialNumber
        self.boxNumber = boxNumber
        self.crateNumber = crateNumber
        self.isDamaged = isDamaged
        self.flashed = flashed
        self.keyInjected = keyInjected
        self.sendForRepacking = sendForRepacking
        self.IMEI = IMEI
        self.deviceState = deviceState
    
    def returnSerialNumber(self):
        return self.serialNumber
    
    def returnIMEI(self):
        return self.IMEI
    
    def setSimCardInfo(self, SNN, IMSI):
        self.simcard = simCardInfo(SNN, IMSI)
    
    def setWarehouseInfo(self, warehouseNumber, sectionNumber, rowNumber, shelfNumber, segmentNumber, segment):
        self.warehouse = warehouseInfo(warehouseNumber, sectionNumber, rowNumber, shelfNumber, segmentNumber, segment)

deviceTest = device(123, 1, 2, False, 3, False, False, 8181, 1)
deviceTest.setSimCardInfo(1, 3)
deviceTest.setWarehouseInfo(1, 2, 3, 4, 5, 1)

