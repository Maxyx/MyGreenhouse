import logging

import smbus

from mygreenhouse.hardware.exceptions import I2CDeviceNotFound


class I2CDevice:
    def __init__(self, address):
        self.address = address
        self.smbus = smbus.SMBus(1)
        self.check_device_detectable()

    def __del__(self):
        self.smbus.close()

    def check_device_detectable(self):
        try:
            self.smbus.write_byte(self.address, 0)
            logging.info('I2C device found at address ' + hex(self.address))
        except OSError:
            logging.warning('I2C device not found at address ' + hex(self.address))
            raise I2CDeviceNotFound(self.address)
