import unittest

from pygeocdse.odata_attributes import get_attribute_type


class TestOdataAttributes(unittest.TestCase):

    def test_get_attribute_type_string(self):
        attribute_name = "platformShortName"
        expected = "String"
        self.assertEqual(expected, get_attribute_type(attribute_name))

    def test_get_attribute_type_integer(self):
        attribute_name = "relativeOrbitNumber"
        expected = "Integer"
        self.assertEqual(expected, get_attribute_type(attribute_name))

    def test_get_attribute_type_double(self):
        attribute_name = "illuminationZenithAngle"
        expected = "Double"
        self.assertEqual(expected, get_attribute_type(attribute_name))

    def test_get_attribute_type_dateoffset(self):
        attribute_name = "processingDate"
        expected = "DateTimeOffset"
        self.assertEqual(expected, get_attribute_type(attribute_name))

    def test_get_attribute_type_not_found(self):
        attribute_name = "not_found"
        with self.assertRaises(ValueError):
            get_attribute_type(attribute_name)
