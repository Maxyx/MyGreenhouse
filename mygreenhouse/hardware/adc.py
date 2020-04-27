from mygreenhouse.hardware.i2c_addresses import I2CAddresses
from mygreenhouse.hardware.i2cdevice import I2CDevice


class PCF8591(I2CDevice):
    def __init__(self, communication_handler):
        super().__init__(I2CAddresses.PCF8591, communication_handler)
