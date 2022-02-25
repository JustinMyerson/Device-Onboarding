import unittest
from device import *
from mockDatabaseRepo import *

class test(unittest.TestCase):
    def testDevice(self):
        self.assertEquals(deviceTest.serialNumber, 123)
        self.assertEquals(deviceTest.boxNumber, 1)
        self.assertEquals(deviceTest.crateNumber, 2)
        self.assertEquals(deviceTest.isDamaged, 99)

    def testDeviceWrittenToMockDatabaseRepo(self):
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEquals(mockDB.getSizeOfListOfDevices(), 1, "Device not added to database")
    
    def testFindDeviceBySerialNumber(self):
        mockSerial = 123
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEquals(mockDB.getDeviceBySerial(mockSerial).returnSerialNumber(), 123, "Device cannot be found with serial number {} ".format(mockSerial))
    
    def testFindDeviceByIMEINumber(self):
        mockIMEI = 8181
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEquals(mockDB.getDeviceByIMEI(mockIMEI).returnIMEI(), 8181, "Device cannot be found with IMEI number {}".format(mockIMEI))

if __name__ == '__main__':
    unittest.main()