import unittest
from unittest.mock import patch

from mygreenhouse.hardware.exceptions import I2CDeviceNotFound
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

    @patch('smbus.SMBus')
    def test_DeviceNotFound_exception_raised_when_device_undetectable(self, mock_smbus):
        device_address = 0x5
        with self.assertRaises(I2CDeviceNotFound) as expected_exception:
            mock_smbus.return_value.write_byte.side_effect = OSError()
            I2CDevice(device_address)
        self.assertEqual(device_address, expected_exception.exception.address)

    @patch('smbus.SMBus')
    def test_read_byte_from_register_called_with_correct_address(self, mock_smbus):
        device_address = 0x2
        d = I2CDevice(device_address)
        register = 0x1
        d.read_byte_from_register(register)
        mock_smbus.return_value.read_byte_data.assert_called_once_with(device_address, register)


if __name__ == '__main__':
    unittest.main()
