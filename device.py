class device:
    def __init__(self, serialNumber, boxNumber, crateNumber, isDamaged, IMEI):
        self.serialNumber = serialNumber
        self.boxNumber = boxNumber
        self.crateNumber = crateNumber
        self.isDamaged = isDamaged
        self.IMEI = IMEI
    
    def returnSerialNumber(self):
        return self.serialNumber
    
    def returnIMEI(self):
        return self.IMEI
    
deviceTest = device(123, 1, 2, 99, 8181)

