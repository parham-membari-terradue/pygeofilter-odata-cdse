import re
from pygeocdse.evaluator import to_cdse
from typing import Dict, List, Optional

"""A dictionary mapping typical STAC collection names (stripped of special characters)
onto CDSE collection names (and optionally product types)"""
collection_map = {
    'sentinel1': ["SENTINEL-1"],
    'sentinel1raw': ["SENTINEL-2", "RAW"],
    'sentinel1grd': ["SENTINEL-1", "GRD"],
    'sentinel1slc': ["SENTINEL-2", "SLC"],
    'sentinel1ocn': ["SENTINEL-2", "OCN"],
    'sentinel2': ["SENTINEL-2"],
    'sentinel2l1c': ["SENTINEL-2", "S2MSI1C"],
    'sentinel2l2a': ["SENTINEL-2", "S2MSI2A"],
    'sentinel3': ["SENTINEL-3"],
    'sentinel5p': ["SENTINEL-5P"],
}

def to_cdse_query(stac_search: Dict) -> Dict:
    
    query = {}
    filter = get_odata_filter(stac_search.get('collections'), stac_search.get('filter'))
    if filter:
        query['$filter'] = filter

    order_by = get_odata_order_by(stac_search.get('sortby'))
    if order_by:
        query['$orderby'] = order_by

    return query
    
    
def to_cdse_query_str(stac_search: Dict) -> str:
    query_str = ''
    filter = get_odata_filter(stac_search.get('collections'), stac_search.get('filter'))
    if filter:
        query_str = "$filter={0}".format(filter)

    order_by = get_odata_order_by(stac_search.get('sortby'))
    if order_by:
        if query_str:
            query_str += "&"
        query_str += "$orderby={0}".format(order_by)

    return query_str


def get_odata_filter(stac_collections, stac_filter):
    collection_filter = get_odata_collection_filter(stac_collections)
    if stac_filter:
        filter = to_cdse(stac_filter)
    else:
        filter = None
    
    if filter:
        if collection_filter:
            return "{0} and {1}".format(collection_filter, filter)
        else:
            return filter
    elif collection_filter:
        return collection_filter


def get_odata_collection_filter(collections: List[str]) -> str:
    result = None
    multiple = False
    
    for collection in collections:
        # Get map key candiate for obtaining CDSE collection and product type query parameters
        name = re.sub("[^a-z0-9]", '', collection.lower())

        # Name can be map key or Map key can be the the given collection name itself or be contained in it
        values = collection_map.get(name) or next((collection_map[k] for k in reversed(collection_map) if name in k), None)

        # No match -> do nothing
        if not values:
            continue

        multiple = result is not None

        if multiple:
            result += " or "

        result = "Collection/Name eq '{0}'".format(values[0])
        if len(values) > 1:
            result += " and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq '{0}')".format(values[1])

    if multiple:
        result = "({0})".format(result)

    return result

def get_odata_order_by(stac_sort_by: List[Dict]) -> str:
    if stac_sort_by is None:
        return
    result = None
    for criterion in stac_sort_by:
        field = criterion.get('field')
        direction = criterion.get('direction')
        if not field: continue
        if result is None:
            result = ''
        else:
            result += ","
        result += field
        if direction in ['asc', 'desc']:
            result += " {0}".format(direction)
    
    return result

