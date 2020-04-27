import unittest
from unittest.mock import MagicMock

from mygreenhouse.hardware.i2cdevice import I2CDevice


class I2CDeviceTests(unittest.TestCase):
    def test_check_device_is_detectable_at_creation(self):
        mock_i2c_com_handler = MagicMock()
        device_address = 0x10
        I2CDevice(device_address, mock_i2c_com_handler)
        mock_i2c_com_handler.check_device_detectable.assert_called_once_with(device_address)


if __name__ == '__main__':
    unittest.main()
