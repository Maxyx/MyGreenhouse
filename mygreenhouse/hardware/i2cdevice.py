class I2CDevice:
    def __init__(self, address, i2c_communication_handler):
        self.address = address
        self.communication_handler = i2c_communication_handler
        self.communication_handler.check_device_detectable(self.address)
