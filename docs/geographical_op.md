## Intersects

`s_intersects` isd, at the moment, the only Geographical supported operator, i.e.

```json
{
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
```

Will be interpreted as

```
OData.CSC.Intersects(area=geography'SRID=4326;POLYGON ((12.655118166047592 47.44667197521409, 21.39065656328509 48.347694733853245, 28.334291357162826 41.877123516783655, 17.47086198383573 40.35854475076158, 12.655118166047592 47.44667197521409))')
```
