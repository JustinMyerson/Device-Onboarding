from simCardInfo import *

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

deviceTest = device(123, 1, 2, False, 3, False, False, 8181, 1)
deviceTest.setSimCardInfo(1, 3)

