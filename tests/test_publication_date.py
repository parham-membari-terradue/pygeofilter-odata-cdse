import unittest

from loguru import logger
from pygeofilter.parsers.cql2_json import parse as json_parse
from pygeofilter.util import IdempotentDict

from pygeocdse.evaluator import to_cdse


# see https://documentation.dataspace.copernicus.eu/APIs/OData.html#query-by-publication-date
# https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=PublicationDate gt 2019-05-15T00:00:00.000Z and PublicationDate lt 2019-05-16T00:00:00.000Z
class TestPublicationDate(unittest.TestCase):

    def setUp(self):
        pass

    '''
    timestamp
    '''

    def test_publication_date_exclusive(self):
        cql2_filter = {
            "op": "and",
            "args": [
                {
                    "op": "t_after",
                    "args": [
                        {"property": "PublicationDate"},
                        {"timestamp": "2023-02-01T00:00:00Z"}
                    ],
                },
                {
                    "op": "t_before",
                    "args": [
                        {"property": "PublicationDate"},
                        {"timestamp": "2023-02-28T23:59:59Z"}
                    ],
                },
            ],
        }
        expected = "PublicationDate gt 2023-02-01T00:00:00+00:00 and PublicationDate lt 2023-02-28T23:59:59+00:00"
        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )

    def test_publication_date_inclusive(self):
        cql2_filter = {
            "op": "and",
            "args": [
                {
                    "op": "t_begins",
                    "args": [
                        {"property": "PublicationDate"},
                        {"timestamp": "2023-02-01T00:00:00Z"}
                    ],
                },
                {
                    "op": "t_ends",
                    "args": [
                        {"property": "PublicationDate"},
                        {"timestamp": "2023-02-28T23:59:59Z"}
                    ],
                },
            ],
        }
        expected = "PublicationDate ge 2023-02-01T00:00:00+00:00 and PublicationDate le 2023-02-28T23:59:59+00:00"
        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )

    '''
    interval
    '''

    def test_publication_date_interval_after(self):
        cql2_filter = {
            "op": "and",
            "args": [
                {
                    "op": "t_after",
                     "args": [
                         {"property": "PublicationDate"},
                         {"interval": ["2023-02-01T00:00:00Z", "2023-02-01T23:59:59Z"]},
                    ]
                },
            ],
        }
        expected = "PublicationDate gt 2023-02-01T00:00:00+00:00 and PublicationDate le 2023-02-01T23:59:59+00:00"
        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )

    def test_publication_date_interval_before(self):
        cql2_filter = {
            "op": "and",
            "args": [
                {
                    "op": "t_before",
                     "args": [
                         {"property": "PublicationDate"},
                         {"interval": ["2023-02-01T00:00:00Z", "2023-02-01T23:59:59Z"]},
                    ]
                },
            ],
        }
        expected = "PublicationDate ge 2023-02-01T00:00:00+00:00 and PublicationDate lt 2023-02-01T23:59:59+00:00"
        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )

    def test_publication_date_interval_begin(self):
        cql2_filter = {
            "op": "and",
            "args": [
                {
                    "op": "t_begins",
                     "args": [
                         {"property": "PublicationDate"},
                         {"interval": ["2023-02-01T00:00:00Z", "2023-02-01T23:59:59Z"]},
                    ]
                },
            ],
        }
        expected = "PublicationDate ge 2023-02-01T00:00:00+00:00 and PublicationDate le 2023-02-01T23:59:59+00:00"
        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )

    def test_publication_date_interval_ends(self):
        cql2_filter = {
            "op": "and",
            "args": [
                {
                    "op": "t_ends",
                     "args": [
                         {"property": "PublicationDate"},
                         {"interval": ["2023-02-01T00:00:00Z", "2023-02-01T23:59:59Z"]},
                    ]
                },
            ],
        }
        expected = "PublicationDate ge 2023-02-01T00:00:00+00:00 and PublicationDate le 2023-02-01T23:59:59+00:00"
        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )

