class device:
    def __init__(self, serialNumber, boxNumber, crateNumber, isDamaged):
        self.serialNumber = serialNumber
        self.boxNumber = boxNumber
        self.crateNumber = crateNumber
        self.isDamaged = isDamaged
    
    
deviceTest = device(123, 1, 2, 99)

