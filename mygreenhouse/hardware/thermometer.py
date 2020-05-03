import math

from mygreenhouse.hardware.exceptions import InvalidTemperature


class Thermometer:
    VOLTAGE_REFERENCE = 3.3
    REFERENCE_TEMPERATURE_KELVIN = 298.15
    RESISTANCE_AT_REFERENCE_TEMPERATURE_KILO = 10
    RESISTANCE_DIVIDER_KILO = 10
    THERMAL_INDEX = 3950.0

    def __init__(self, adc, adc_thermistor_channel):
        self.adc = adc
        self.adc_channel = adc_thermistor_channel

    def get_temperature_celsius(self):
        value_from_adc = self.adc.analog_read_of_channel(self.adc_channel)
        if value_from_adc < 0 or value_from_adc > self.adc.MAX_VALUE:
            raise InvalidTemperature(value_from_adc)

        thermistor_voltage = (value_from_adc * self.VOLTAGE_REFERENCE) / self.adc.MAX_VALUE
        thermistor_resistance = self.RESISTANCE_DIVIDER_KILO * thermistor_voltage / \
                                (self.VOLTAGE_REFERENCE - thermistor_voltage)
        temperature_kelvin = 1 / (1 / self.REFERENCE_TEMPERATURE_KELVIN +
                                  math.log(thermistor_resistance / self.RESISTANCE_AT_REFERENCE_TEMPERATURE_KILO)
                                  / self.THERMAL_INDEX)
        temperature_celsius = temperature_kelvin - 273.15
        return round(temperature_celsius)
