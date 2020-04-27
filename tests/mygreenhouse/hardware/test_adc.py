import unittest

from mygreenhouse.hardware.adc import PCF8591
from mygreenhouse.hardware.i2c_addresses import I2CAddresses


class PCF8591Tests(unittest.TestCase):
    def test_correct_I2C_address_used_for_PCF8591(self):
        self.assertEqual(I2CAddresses.PCF8591, PCF8591().address)


if __name__ == '__main__':
    unittest.main()
