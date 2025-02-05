# pygeofilter CDSE OData support for CQL2

## Scope

We aim to provide users a simpler [OData](https://www.odata.org/) Filtering experience by let them expressing a [$filter](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#_Toc31358948) via [Common Query Language](https://www.ogc.org/publications/standard/cql2/) (also known as _CQL2_).

## Target

This library, written in Python, is developed to simplify System Integrators daily routines to interact with Geospatial catalogs, such as the [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/).

## Usage

Once the library is installed, everything required are the following steps:

```python
from pygeocdse.evaluator import http_invoke

# define the OData catalog base URL

base_url = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"

# define the OData filter, according to CQL2 (JSON)

cql2_filter =  = {
    "op": "and",
    "args": [
        {
            "op": "eq",
            "args": [
                {"property": "Collection/Name"},
                "SENTINEL-2"
            ]
        },
        {
            "op": "eq",
            "args": [
                {"property": "productType"},
                "S2MSI1C"
            ]
        },
        {
            "op": "s_intersects",
            "args": [
                {"property": "geometry"},
                {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-11, 35],
                            [27.5, 35],
                            [27.5, 60],
                            [-11, 60],
                            [-11, 35],
                        ]
                    ],
                },
            ],
        }
    ],
}

# Now query the OData Catalog via HTTP

data = http_invoke(base_url, cql2_filter)

# manipulate resulting data

```

## Disclaimer

This is Work in Progress, only a limited subset of OData operators are supported for CDSE use cases only.

Contributions are welcome and appreciated.
