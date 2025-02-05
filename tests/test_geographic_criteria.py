import unittest

from loguru import logger
from pygeofilter.parsers.cql2_json import parse as json_parse
from pygeofilter.util import IdempotentDict

from pygeocdse.evaluator import to_cdse


# see https://documentation.dataspace.copernicus.eu/APIs/OData.html#query-by-geographic-criteria
class TestGeographicCriteria(unittest.TestCase):

    def setUp(self):
        pass

    def test_search_polygon(self):
        # To search for products intersecting the specified polygon
        cql2_filter = {
            "op": "and",
            "args": [
                {
                    "op": "s_intersects",
                    "args": [
                        {"property": "geometry"},
                        {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [12.655118166047592, 47.44667197521409],
                                    [21.39065656328509, 48.347694733853245],
                                    [28.334291357162826, 41.877123516783655],
                                    [17.47086198383573, 40.35854475076158],
                                    [12.655118166047592, 47.44667197521409],
                                ]
                            ],
                        },
                    ],
                },
            ],
        }

        expected = "OData.CSC.Intersects(area=geography'SRID=4326;POLYGON ((12.655118166047592 47.44667197521409, 21.39065656328509 48.347694733853245, 28.334291357162826 41.877123516783655, 17.47086198383573 40.35854475076158, 12.655118166047592 47.44667197521409))')"

        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )

    def test_search_point(self):
        # To search for products intersecting the specified point
        cql2_filter = {
            "op": "s_intersects",
            "args": [
                {"property": "geometry"},
                {
                    "type": "Point",
                    "coordinates": [12.655118166047592, 47.44667197521409],
                },
            ],
        }

        expected = "OData.CSC.Intersects(area=geography'SRID=4326;POINT (12.655118166047592 47.44667197521409)')"

        self.assertEqual(
            expected, to_cdse(cql2_filter)
        )
