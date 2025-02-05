| Description                                                    | CQL2 Operator | Resulting OData Operator |
|----------------------------------------------------------------|---------------|--------------------------|
| The subject is a temporal entity that occurs after the object  | `t_after`     | `gt`                     |
| The subject is a temporal entity that occurs before the object | `t_before`    | `lt`                     |
| Beginning of a temporal entity.                                | `t_begins`    | `ge`                     |
| End of a temporal entity.                                      | `t_ends`      | `le`                     |


## Sample

Given the CQL2 snippet:

```json
{
    "op": "and",
    "args": [
        {
            "op": "t_after",
            "args": [
                {"property": "ContentDate/Start"},
                {"timestamp": "2023-02-01T00:00:00Z"}
            ],
        },
        {
            "op": "t_before",
            "args": [
                {"property": "ContentDate/Start"},
                {"timestamp": "2023-02-28T23:59:59Z"}
            ],
        },
    ],
}
```

It will be translated to OData as:

```
ContentDate/Start gt 2023-02-01T00:00:00+00:00 and ContentDate/Start lt 2023-02-28T23:59:59+00:00
```

Please take note that the ISO format for dates in OData are internally handled, so users can express dates in CQL2 supported formats.

## Intervals

Intervals are supported for a single property, they are limits inclusive by default, the `op` has to be accurately tuned, i.e. the CQL2 snippet below:

```json
{
    "op": "and",
    "args": [
        {
            "op": "t_after",
            "args": [
                {"property": "ContentDate/Start"},
                {"interval": ["2023-02-01T00:00:00Z", "2023-02-01T23:59:59Z"]},
            ],
        },
        {
            "op": "t_before",
            "args": [
                {"property": "ContentDate/End"},
                {"interval": ["2023-02-28T00:00:00Z", "2023-02-28T23:59:59Z"]}
            ],
        },
    ]
}
```

It will be translated to OData as:

```
ContentDate/Start gt 2023-02-01T00:00:00+00:00 and ContentDate/Start le 2023-02-01T23:59:59+00:00 and ContentDate/End ge 2023-02-28T00:00:00+00:00 and ContentDate/End lt 2023-02-28T23:59:59+00:00"
```

