class I2CDeviceNotFound(Exception):
    def __init__(self, device_i2c_address):
        self.address = device_i2c_address

    def __str__(self):
        return 'I2C device not found at address ' + hex(self.address)
