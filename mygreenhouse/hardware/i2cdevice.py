import smbus


class I2CDevice:
    def __init__(self, address):
        self.address = address
        self.smbus = smbus.SMBus(1)
        self.check_device_detectable()

    def __del__(self):
        self.smbus.close()

    def check_device_detectable(self):
        self.smbus.write_byte(self.address, 0)
