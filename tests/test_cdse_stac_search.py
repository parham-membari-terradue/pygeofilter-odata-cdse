import unittest

from loguru import logger
from pygeofilter.parsers.cql2_json import parse as json_parse
from pygeofilter.util import IdempotentDict
import json
from pygeocdse.search import to_cdse_query, to_cdse_query_str, stac_search_map


class TestCDSEEvaluator(unittest.TestCase):

    search_basic_filter = {
        "collections": [
            "SENTINEL-2"
        ]
    }

    search_collection_filter = {
        "collections": [
            "sentinel-2-l2a"
        ],
        "filter-lang": "cql2-json",
        "filter": {
            "op": "and",
            "args": [
                {
                    "op": "=",
                    "args": [
                        { "property": "platformSerialIdentifier" },
                        "B"
                    ]
                }
            ],
        },
        #"sortby": [
        #    {
        #    "field": "id",
        #    "direction": "asc"
        #    }
        #]
    }

    search_date = {
    }

    search_sort = {
        "collections": [
            "SENTINEL-1"
        ],
        "filter-lang": "cql2-json",
        "filter": {
            "op": "and",
            "args": [
                {
                    "op": "=",
                    "args": [
                        { "property": "platformSerialIdentifier" },
                        "B"
                    ]
                }
            ],
        },
        "sortby": [
            {
            "field": "ContentDate/Start",
            "direction": "desc"
            }
        ]
    }

    search_map = {
        "collections": [ "SENTINEL-2" ],
        "filter-lang": "cql2-json",
        "filter": {
            "op": "=",
            "args": [ { "property": "constellation" }, "sentinel-2" ]
        }
    }

    search_map_platform = {
        "collections": [ "SENTINEL-2" ],
        "filter-lang": "cql2-json",
        "filter": {
            "op": "=",
            "args": [ { "property": "platform" }, "sentinel-2a" ]
        }
    }


    def setUp(self):
        pass

    def test_search_basic_filter(self):
        expected = {
            "$filter": "Collection/Name eq 'SENTINEL-2'"
        }
        actual = to_cdse_query(self.__class__.search_basic_filter)
        print(actual)
        self.assertDictEqual(expected, actual)

    def test_search_basic_filter_str(self):
        expected = "$filter=Collection/Name eq 'SENTINEL-2'"
        actual = to_cdse_query_str(self.__class__.search_basic_filter)
        self.assertEqual(expected, actual)


    def test_search_collection_filter(self):
        expected = {
            "$filter": "Collection/Name eq 'SENTINEL-2' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S2MSI2A') and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformSerialIdentifier' and att/OData.CSC.StringAttribute/Value eq 'B')"
        }
        actual = to_cdse_query(self.__class__.search_collection_filter)
        self.assertDictEqual(expected, actual)

    def test_search_collection_filter_str(self):
        expected = "$filter=Collection/Name eq 'SENTINEL-2' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S2MSI2A') and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformSerialIdentifier' and att/OData.CSC.StringAttribute/Value eq 'B')"
        actual = to_cdse_query_str(self.__class__.search_collection_filter)
        self.assertEqual(expected, actual)

    def test_search_sort(self):
        expected = {
            '$filter': "Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformSerialIdentifier' and att/OData.CSC.StringAttribute/Value eq 'B')",
            '$orderby': 'ContentDate/Start desc'
        }
        actual = to_cdse_query(self.__class__.search_sort)
        self.assertDictEqual(expected, actual)

    def test_search_sort_str(self):
        expected = "$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformSerialIdentifier' and att/OData.CSC.StringAttribute/Value eq 'B')&$orderby=ContentDate/Start desc"
        actual = to_cdse_query_str(self.__class__.search_sort)
        self.assertEqual(expected, actual)

    def test_search_map(self):
        expected = {
            '$filter': "Collection/Name eq 'SENTINEL-2' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformShortName' and att/OData.CSC.StringAttribute/Value eq 'SENTINEL-2')"
        }
        actual = to_cdse_query(self.__class__.search_map)
        self.assertEqual(expected, actual)

    def test_search_map_str(self):
        expected = "$filter=Collection/Name eq 'SENTINEL-2' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformShortName' and att/OData.CSC.StringAttribute/Value eq 'SENTINEL-2')"
        actual = to_cdse_query_str(self.__class__.search_map)
        self.assertEqual(expected, actual)

    def test_search_map_platform(self):
        expected = {
            '$filter': "Collection/Name eq 'SENTINEL-2' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformShortName' and att/OData.CSC.StringAttribute/Value eq 'SENTINEL-2') and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformSerialIdentifier' and att/OData.CSC.StringAttribute/Value eq 'A')"
        }
        actual = to_cdse_query(self.__class__.search_map_platform)
        print(actual)
        self.assertEqual(expected, actual)
        # self.assertEqual(1, 1)
