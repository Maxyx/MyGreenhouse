import unittest
from unittest.mock import MagicMock

from mygreenhouse.hardware.adc import PCF8591
from mygreenhouse.hardware.i2c_addresses import I2CAddresses


class PCF8591Tests(unittest.TestCase):
    def test_correct_I2C_address_used_for_PCF8591(self):
        self.assertEqual(I2CAddresses.PCF8591.value, PCF8591(MagicMock()).address)

    def test_analog_read_from_channel_reads_correct_register(self):
        mock_i2c = MagicMock()
        adc = PCF8591(mock_i2c)
        channels_registers = [0x40, 0x41, 0x42, 0x43]
        for i in range(4):
            with self.subTest(msg='Correct register read for channel {}'.format(i), i=i):
                adc.analog_read_of_channel(i)
                mock_i2c.read_byte_from_register.assert_called_with(adc.address, channels_registers[i])


if __name__ == '__main__':
    unittest.main()
