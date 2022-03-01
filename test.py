from doctest import testmod
import unittest
from device import *
from mockDatabaseRepo import *
from inputHandler import *
from mockFlashDevice import flashDevice, mockFlashDevice
from mockKeyInjection import *
from deviceState import *

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
        mockDB.appendToDeviceList(deviceTest)
        mockDB.appendToDeviceList(inputHandler.userInput)
        self.assertEquals(mockDB.getSizeOfListOfDevices(), 2, "Device not added to database")
    
    def testDeviceStateUpdated(self):
        self.assertEquals(deviceTest.getDeviceState(), "STORED_IN_WAREHOUSE")

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
        self.assertEquals(mockDB.checkIfFlashed(mockIMEI), False)
    
    def testCheckDeviceKeyInjected(self):
        mockIMEI = 8181
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEquals(mockDB.checkIfKeyInjected(mockIMEI), False)
    
    def testFlashDevice(self):
        mockFlash = mockFlashDevice()
        flashDevice(mockFlash)

    def testUpdateFlashedAndUpdateKeys(self):
        deviceTest.updateFlashed()
        deviceTest.updateKeys(12345)
        self.assertTrue(deviceTest.returnFlashed, "Device has not updated the flashed property")
        self.assertEquals(deviceTest.keyInjected, 12345, "Key not added correctly")
    
    def testDeviceDamaged(self):
        self.assertEquals(deviceDamageTest.getDeviceState(), "DAMAGE_RECORDED", "Device damage is not recorded correctly")
        self.assertEquals(deviceDamageTest.returnIMEI(), None, "Device damage is not recorded correctly")

if __name__ == '__main__':
    print("Welcome / Welkom / Shalom")
    print("Please choose device state to start with from the following options:")
    count = 0
    for d in deviceState:
        print("{} - {}".format(count, d.name))
        count += 1
    
    unittest.main()