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
        self.assertEqual(deviceTest.serialNumber, 123)
        self.assertEqual(deviceTest.boxNumber, 1)
        self.assertEqual(deviceTest.crateNumber, 2)
    
    def testSimCardInfo(self):
        self.assertEqual(deviceTest.simcard.IMSI, 3, "Device sim card information not stored correctly")
    
    def testWarehouseInfo(self):
        self.assertEqual(deviceTest.warehouse.warehouseNumber, 1, "Warehouse information not stored correctly")

    def testDeviceWrittenToMockDatabaseRepo(self):     
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        mockDB.appendToDeviceList(inputHandler.userInput)
        self.assertEqual(mockDB.getSizeOfListOfDevices(), 2, "Device not added to database")
    
    def testDeviceStateUpdated(self):
        self.assertEqual(deviceTest.getDeviceState(), "STORED_IN_WAREHOUSE")

    def testFindDeviceBySerialNumber(self):
        mockSerial = 123
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEqual(mockDB.getDeviceBySerial(mockSerial).returnSerialNumber(), 123, "Device cannot be found with serial number {} ".format(mockSerial))
    
    def testFindDeviceByIMEINumber(self):
        mockIMEI = 8181
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEqual(mockDB.getDeviceByIMEI(mockIMEI).returnIMEI(), 8181, "Device cannot be found with IMEI number {}".format(mockIMEI))

    def testCheckDeviceFlashed(self):
        mockIMEI = 8181
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEqual(mockDB.checkIfFlashed(mockIMEI), False)
    
    def testCheckDeviceKeyInjected(self):
        mockIMEI = 8181
        mockDB = mockDatabaseRepo()
        mockDB.appendToDeviceList(deviceTest)
        self.assertEqual(mockDB.checkIfKeyInjected(mockIMEI), False)
    
    def testFlashDevice(self):
        mockFlash = mockFlashDevice()
        flashDevice(mockFlash)

    def testUpdateFlashedAndUpdateKeys(self):
        deviceTest.updateFlashed()
        deviceTest.updateKeys(12345)
        self.assertTrue(deviceTest.returnFlashed, "Device has not updated the flashed property")
        self.assertEqual(deviceTest.keyInjected, 12345, "Key not added correctly")
    
    def testDeviceDamaged(self):
        self.assertEqual(deviceDamageTest.getDeviceState(), "DAMAGE_RECORDED", "Device damage is not recorded correctly")
        self.assertEqual(deviceDamageTest.returnIMEI(), None, "Device damage is not recorded correctly")  

if __name__ == '__main__':
    unittest.main()
    
