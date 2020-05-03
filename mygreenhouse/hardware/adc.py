from mygreenhouse.hardware.exceptions import NoDeviceAtADCChannel
from mygreenhouse.hardware.i2c_addresses import I2CAddresses
from mygreenhouse.hardware.i2cdevice import I2CDevice


class PCF8591(I2CDevice):
    MAX_VALUE = 255
    NO_DEVICE = MAX_VALUE

    def __init__(self, communication_handler):
        super().__init__(I2CAddresses.PCF8591.value, communication_handler)
        self.standard_command = 0x40

    def analog_read_of_channel(self, channel):
        value = self.communication_handler.read_byte_from_register(self.address, self.standard_command + channel)
        if value == self.NO_DEVICE:
            raise NoDeviceAtADCChannel(self.address, channel)
        return value
