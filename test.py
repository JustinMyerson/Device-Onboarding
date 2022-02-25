import unittest
from device import *
from mockDatabaseRepo import *

class test(unittest.TestCase):
    def testDevice(self):
        self.assertEquals(deviceTest.serialNumber, 123)
        self.assertEquals(deviceTest.boxNumber, 1)
        self.assertEquals(deviceTest.crateNumber, 2)
    
    def testSimCardInfo(self):
        self.assertEquals(deviceTest.simcard.IMSI, 3, "Device sim card information not stored correctly")

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
    print("Welcome / Welkom / Shalom")
    # serialNumber = input("Enter device serial number: ")
    # boxNumber = input("Enter device box number: ")
    # crateNumber = input("Enter device crate number: ")
    # damaged = input("Enter damage from 1-5: ")
    # snn = input("Enter snn number: ")
    # imsi = input("Enter imsi number: ")
    # flashed = input("Is device flashed (True/False): ")
    # keyInjected = input("Is device key injected (True/False): ")
    # sendForRepacking = input("Device needs to be repacked (True/False): ")
    unittest.main()