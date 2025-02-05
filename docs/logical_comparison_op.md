# Supported Comparison operators

| Description           | CQL2 Operator(s) | Resulting OData Operator |
|-----------------------|------------------|--------------------------|
| Equal                 | `=`, `eq`        | `eq`                     |
| Greater than          | `>`,`gt`         | `gt`                     |
| Greater than or equal | `>=`,`gte`       | `ge`                     |
| Less than             | `<`, `lt`        | `lt`                     |
| Less than or equal    | `<=`, `lte`      | `le`                     |

## Sample

Given the CQL2 snippet:

```json
{
    "op": "and",
    "args": [
        {
            "op": "<CQL2_COMPARISON_OPERATOR>",
            "args": [
                {"property": "cloudCover"},
                20
            ]
        }
    ],
}
```

It will be translated to OData as:

```
Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value <TRANSLATED_ODATA__COMPARISON_OPERATOR> 20)
```

Please take note that `Collection/Name` is a reserved keyword, so the CQL2 snippet below:

```json
{
    "op": "and",
    "args": [
        {
            "op": "eq",
            "args": [
                {"property": "Collection/Name"},
                "SENTINEL-2"
            ]
        }
    ],
}
```

It will be translated to OData as:

```
Collection/Name eq 'SENTINEL-2'
```

# Supported inclusion operators

| Description           | CQL2 Operator(s) | Resulting OData Operator |
|-----------------------|------------------|--------------------------|
| Is a member of        | `in`             | `in`                     |

## Sample

Given the CQL2 snippet:

```json
{
    "op": "in",
    "args": [
        {"property": "productType"},
        [
            "IW_GRHD_1S",
            "IW_GRDH_1S",
            "EW_GRDM_1S",
            "EW_GRDH_1S",
            "S1_GRDH_1S",
            "S2_GRDH_1S",
            "S3_GRDH_1S",
            "S4_GRDH_1S",
            "S5_GRDH_1S",
            "S6_GRDH_1S"
        ]
    ]
}
```

It will be translated to OData as:

```
(Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_GRHD_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_GRDH_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDM_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDH_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S1_GRDH_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S2_GRDH_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S3_GRDH_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S4_GRDH_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S5_GRDH_1S') or Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S6_GRDH_1S'))
```

# Supported Logical operators

| Description | CQL2 Operator(s) | Resulting OData Operator |
|-------------|------------------|--------------------------|
| Logical and | `and`            | `and`                    |
| Logical or  | `or`             | `or`                     |
