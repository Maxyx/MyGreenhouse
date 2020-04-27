import logging

import smbus

from mygreenhouse.hardware.exceptions import I2CDeviceNotFound


class I2CDevice:
    def __init__(self, address):
        self.address = address
        self.bus = smbus.SMBus(1)
        self.check_device_detectable()

    def __del__(self):
        self.bus.close()

    def check_device_detectable(self):
        try:
            self.bus.write_byte(self.address, 0)
            logging.info('I2C device found at address ' + hex(self.address))
        except OSError:
            logging.warning('I2C device not found at address ' + hex(self.address))
            raise I2CDeviceNotFound(self.address)

    def read_byte_from_register(self, register):
        self.bus.read_byte_data(self.address, register)
