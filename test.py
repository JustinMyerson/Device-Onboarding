import unittest
from device import *

class test(unittest.TestCase):
    def testDevice(self):
        self.assertEquals(deviceTest.serialNumber, 123)
        self.assertEquals(deviceTest.boxNumber, 1)
        self.assertEquals(deviceTest.crateNumber, 2)
        self.assertEquals(deviceTest.isDamaged, 99)

if __name__ == '__main__':
    unittest.main()