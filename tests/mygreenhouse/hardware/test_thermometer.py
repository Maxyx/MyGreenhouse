import unittest
from unittest.mock import MagicMock

from mygreenhouse.hardware.exceptions import InvalidTemperature
from mygreenhouse.hardware.thermometer import Thermometer


class ThermometerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_adc = MagicMock()
        self.mock_adc.MAX_VALUE = 255

    def test_temperature_calculated_properly_from_voltage_read_from_adc(self):
        self.mock_adc.analog_read_of_channel.return_value = 140
        self.assertEqual(21, Thermometer(self.mock_adc, 0).get_temperature_celsius())

    def test_thermometer_raises_InvalidTemperature_when_receiving_negative_value_from_ADC(self):
        negative_adc_value = -1
        self.mock_adc.analog_read_of_channel.return_value = negative_adc_value
        with self.assertRaises(InvalidTemperature) as expected_exception:
            Thermometer(self.mock_adc, 0).get_temperature_celsius()
        self.assertEqual(negative_adc_value, expected_exception.exception.value_read_from_adc)

    def test_thermometer_raises_InvalidTemperature_when_receiving_value_above_ADC_threshold_from_ADC(self):
        value_above_max_adc_value = self.mock_adc.MAX_VALUE + 1
        self.mock_adc.analog_read_of_channel.return_value = value_above_max_adc_value
        with self.assertRaises(InvalidTemperature) as expected_exception:
            Thermometer(self.mock_adc, 0).get_temperature_celsius()
        self.assertEqual(value_above_max_adc_value, expected_exception.exception.value_read_from_adc)


if __name__ == '__main__':
    unittest.main()
