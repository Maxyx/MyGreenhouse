import logging

import smbus2

from mygreenhouse.hardware.exceptions import I2CDeviceNotFound


class I2CCommunicationHandler:
    @staticmethod
    def check_device_detectable(device_i2c_address):
        try:
            I2CCommunicationHandler.write_byte(device_i2c_address, 0)
            logging.info('I2C device found at address ' + hex(device_i2c_address))
            return True
        except OSError:
            logging.warning('I2C device not found at address ' + hex(device_i2c_address))
            raise I2CDeviceNotFound(device_i2c_address)

    @staticmethod
    def write_byte(i2c_address, byte_to_send):
        with smbus2.SMBus(1) as bus:
            bus.write_byte(i2c_address, byte_to_send)

    @classmethod
    def read_byte_from_register(cls, i2c_address, register):
        with smbus2.SMBus(1) as bus:
            return bus.read_byte_data(i2c_address, register)
