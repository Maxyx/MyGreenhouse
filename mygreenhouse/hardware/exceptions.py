class I2CDeviceNotFound(Exception):
    def __init__(self, device_i2c_address):
        self.address = device_i2c_address

    def __str__(self):
        return 'I2C device not found at address ' + hex(self.address)


class NoDeviceAtADCChannel(Exception):
    def __init__(self, adc_address, channel):
        self.adc_address = adc_address
        self.channel = channel

    def __str__(self):
        return 'No device found at channel {} of ADC at address {}'.format(hex(self.channel), hex(self.adc_address))


class InvalidTemperature(Exception):
    def __init__(self, value_read_from_adc):
        self.value_read_from_adc = value_read_from_adc

    def __str__(self):
        return "Value {} read from ADC can't be translated to temperature".format(self.value_read_from_adc)
