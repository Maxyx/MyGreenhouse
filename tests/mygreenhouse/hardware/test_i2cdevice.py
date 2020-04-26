import unittest
from unittest.mock import patch


from mygreenhouse.hardware.i2cdevice import I2CDevice


class I2CDeviceTests(unittest.TestCase):
    @patch('smbus.SMBus')
    def test_connection_checked_at_device_creation_when_device_exists(self, mock_smbus):
        DEVICE_ADDRESS = 0x10
        I2CDevice(DEVICE_ADDRESS)
        mock_smbus.return_value.write_byte.assert_called_once_with(DEVICE_ADDRESS, 0)

    @patch('smbus.SMBus')
    def test_bus_closed_at_object_deletion(self, mock_smbus):
        def assign_and_delete():
            d1 = I2CDevice(0x10)
            d2 = I2CDevice(0x20)
        assign_and_delete()
        self.assertEqual(2, mock_smbus.return_value.close.call_count)


if __name__ == '__main__':
    unittest.main()
