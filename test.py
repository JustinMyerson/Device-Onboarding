import unittest
from device import *
from mockDatabaseRepo import *
from inputHandler import *
from mockKeyInjection import *

class test(unittest.TestCase):
    def testDevice(self):
        self.assertEquals(deviceTest.serialNumber, 123)
        self.assertEquals(deviceTest.boxNumber, 1)
        self.assertEquals(deviceTest.crateNumber, 2)
    
    def testSimCardInfo(self):
        self.assertEquals(deviceTest.simcard.IMSI, 3, "Device sim card information not stored correctly")
    
    def testWarehouseInfo(self):
        self.assertEquals(deviceTest.warehouse.warehouseNumber, 1, "Warehouse information not stored correctly")

    def testDeviceWrittenToMockDatabaseRepo(self):
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(inputHandler.userInput)
        mockDB.appendToDeviceList(deviceTest)
        self.assertEquals(mockDB.getSizeOfListOfDevices(), 2, "Device not added to database")

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

    def testCheckDeviceFlashed(self):
        mockIMEI = 8181
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEquals(mockDB.checkIfFlashed(mockIMEI), True)
    
    def testCheckDeviceKeyInjected(self):
        mockIMEI = 8181
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEquals(mockDB.checkIfKeyInjected(mockIMEI), False)
    
    def testInjectKey(self):
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        mockKey = mockKeyInjection()
        keyInject = keyInjector(deviceTest)
        keyInject.injectKey(mockKey)

if __name__ == '__main__':
    print("Welcome / Welkom / Shalom")
    unittest.main()