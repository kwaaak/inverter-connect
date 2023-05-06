from unittest import TestCase

from inverter.data_types import Config, Parameter
from inverter.definitions import get_definition, get_parameter
from inverter.utilities.modbus_converter import parse_number


class DefinitionsTestCase(TestCase):
    def test_get_definition(self):
        config = Config(inverter_name='deye_2mppt', verbose=False)
        result = get_definition(config=config)
        self.assertIsInstance(result, list)
        example = result[0]['items'][0]
        self.assertEqual(
            example,
            {
                'class': 'voltage',
                'icon': 'mdi:solar-power',
                'name': 'PV1 Voltage',
                'registers': [109],
                'rule': 1,
                'scale': 0.1,
                'state_class': 'measurement',
                'uom': 'V',
            },
        )

    def test_get_parameter(self):
        config = Config(inverter_name='deye_2mppt', verbose=False)
        parameters = get_parameter(config=config)
        self.assertIsInstance(parameters, list)
        example = parameters[0]
        self.assertEqual(
            example,
            Parameter(
                start_register=109,
                length=1,
                group='solar',
                name='PV1 Voltage',
                device_class='voltage',
                state_class='measurement',
                unit='V',
                scale=0.1,
                parser=example.parser,
                offset=None,
                lookup=None,
            ),
        )
        self.assertIs(example.parser, parse_number)
