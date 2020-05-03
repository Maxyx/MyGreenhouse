import unittest
from unittest.mock import patch

from mygreenhouse.hardware.exceptions import I2CDeviceNotFound
from mygreenhouse.hardware.i2c_communication import I2CCommunicationHandler


class I2CCommunicationHandlerTests(unittest.TestCase):
    @patch('smbus2.SMBus')
    def test_device_detected_when_device_detectable(self, mock_smbus):
        device_address = 0x10
        self.assertTrue(I2CCommunicationHandler.check_device_detectable(device_address))
        mock_smbus.return_value.__enter__.return_value.write_byte.assert_called_once_with(device_address, 0)

    @patch('smbus2.SMBus')
    def test_DeviceNotFound_exception_raised_when_device_undetectable(self, mock_smbus):
        device_address = 0x5
        with self.assertRaises(I2CDeviceNotFound) as expected_exception:
            mock_smbus.return_value.__enter__.return_value.write_byte.side_effect = OSError()
            I2CCommunicationHandler().check_device_detectable(device_address)
        self.assertEqual(device_address, expected_exception.exception.address)

    @patch('smbus2.SMBus')
    def test_read_byte_from_register_calls_smbus_read_byte_data_with_correct_addresses(self, mock_smbus):
        device_address = 0x2
        register = 0x1
        expected_byte_to_read = 0x3
        mock_smbus.return_value.__enter__.return_value.read_byte_data.return_value = expected_byte_to_read

        byte_read = I2CCommunicationHandler.read_byte_from_register(device_address, register)
        self.assertEqual(expected_byte_to_read, byte_read)
        mock_smbus.return_value.__enter__.return_value.read_byte_data.assert_called_once_with(device_address, register)


if __name__ == '__main__':
    unittest.main()
