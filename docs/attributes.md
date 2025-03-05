# Supported attributes

As stated, this library was initially developed to support CDSE use cases only, so please make sure the parameters users can query.

## Sentinel-1

| Name                              | Type             | STAC property                    |
|-----------------------------------|------------------|----------------------------------|
| `platformShortName`               | `String`         | `constellation`                  |
| `platformSerialIdentifier`        | `String`         | `platform`                       |
| `productType`                     | `String`         | `product:type`                   |
| `orbitNumber`                     | `Integer`        | `sat:absolute_orbit`             |
| `relativeOrbitNumber`             | `Integer`        | `sat:relative_orbit`             |
| `orbitDirection`                  | `String`         | `sat:orbit_state`                |
| `processorName`                   | `String`         | `processing:software`            |
| `processorVersion`                | `String`         | `processing:software`            |
| `processingCenter`                | `String`         | `processing:facility`            |
| `operationalMode`                 | `String`         | `sar:instrument_mode`            |
| `polarisationChannels`            | `String`         | `sar:polarizations`              |
| `datatakeID`                      | `Integer`        | `s1:datatake_id`                 |
| `swathIdentifier`                 | `String`         | `s1:swaths`                      |
| `timeliness`                      | `String`         | `s1:product_timeliness`          |
| `sliceNumber`                     | `Integer`        | `s1:slice_number`                |
| `totalSlices`                     | `Integer`        | `s1:total_slices`                |
| `instrumentConfigurationID`       | `Integer`        | `s1:instrument_configuration_ID` |
| `processingDate`                  | `DateTimeOffset` | `s1:processing_datetime`         |
| `processingLevel`                 | `String`         | `s1:processing_level`            |
| `coordinates`                     | `String`         |                                  |
| `cycleNumber`                     | `Integer`        |                                  |
| `instrumentShortName`             | `String`         |                                  |
| `segmentStartTime`                | `DateTimeOffset` |                                  |
| `sliceProductFlag`                | `Boolean`        |                                  |
| `origin`                          | `String`         |                                  |
| `productGeneration`               | `DateTimeOffset` |                                  |
| `processingBaseline`              | `String`         |                                  |
| `productClass`                    | `String`         |                                  |
| `productComposition`              | `String`         |                                  |
| `productConsolidation`            | `String`         |                                  |
| `startTimeFromAscendingNode`      | `Double`         |                                  |
| `completionTimeFromAscendingNode` | `Double`         |                                  |

## Sentinel-1-RTC

| Name                       | Type      | STAC property         |
|----------------------------|-----------|-----------------------|
| `platformShortName`        | `String`  | `constellation`       |
| `platformSerialIdentifier` | `String`  | `platform`            |
| `productType`              | `String`  | `product:type`        |
| `instrumentShortName`      | `String`  | `instruments`         |
| `orbitNumber`              | `Integer` | `sat:absolute_orbit`  |
| `relativeOrbitNumber`      | `Integer` | `sat:relative_orbit`  |
| `orbitDirection`           | `String`  | `sat:orbit_state`     |
| `operationalMode`          | `String`  | `sar:instrument_mode` |
| `polarisationChannels`     | `String`  | `sar:polarizations`   |
| `processingLevel`          | `String`  | `s1:processing_level` |
| `spatialResolution`        | `Integer` |                       |
| `authority`                | `String`  |                       |

## Sentinel-2

| Name                       | Type             | STAC property            |
|----------------------------|------------------|--------------------------|
| `platformShortName`        | `String`         | `constellation`          |
| `platformSerialIdentifier` | `String`         | `platform`               |
| `instrumentShortName`      | `String`         | `instruments`            |
| `productType`              | `String`         | `product:_type`          | 
| `orbitNumber`              | `Integer`        | `sat:absolute_orbit`     |
| `relativeOrbitNumber`      | `Integer`        | `sat:relative_orbit`     |
| `processingCenter`         | `String`         | `processing:facility`    |
| `cloudCover`               | `Double`         | `eo:cloud_cover`         |
| `datastripId`              | `String`         | `s2:datastrip_id`        |
| `tileId`                   | `String`         | `s2:tile_id`             |
| `processorVersion`         | `String`         | `s2:processing_baseline` |
| `origin`                   | `String`         |                          |
| `coordinates`              | `String`         |                          |
| `qualityInfo`              | `Integer`        |                          |
| `qualityStatus`            | `String`         |                          |
| `sourceProduct`            | `String`         |                          |
| `processingDate`           | `DateTimeOffset` |                          |
| `productGroupId`           | `String`         |                          |
| `lastOrbitNumber`          | `Integer`        |                          |
| `operationalMode`          | `String`         |                          |
| `processingLevel`          | `String`         |                          | 
| `granuleIdentifier`        | `String`         |                          |
| `processingBaseline`       | `String`         |                          |
| `illuminationZenithAngle`  | `Double`         |                          |
| `sourceProductOriginDate`  | `String`         |                          |

## Sentinel-3

| Name                       | Type             | STAC property              |
|----------------------------|------------------|----------------------------|
| `platformShortName`        | `String`         | `constellation`            |
| `platformSerialIdentifier` | `String`         | `platform`                 |
| `instrumentShortName`      | `String`         | `instruments`              |
| `productType`              | `String`         | `product:type`             |
| `orbitNumber`              | `Integer`        | `sat:absolute_orbit`       |
| `relativeOrbitNumber`      | `Integer`        | `sat:relative_orbit`       |
| `orbitDirection`           | `String`         | `sat:orbit_state`          |
| `processorName`            | `String`         | `processing:software`      |
| `processorVersion`         | `String`         | `processing:software`      |
| `processingCenter`         | `String`         | `processing:facility`      |
| `cloudCover`               | `Double`         | `eo:cloud_cover`           |
| `timeliness`               | `String`         | `s3:processing_timeliness` |
| `landCover`                | `Double`         | `s3:land`                  |
| `coastalCover`             | `Double`         | `s3:coastal`               |
| `brightCover`              | `Double`         |                            |
| `coordinates`              | `String`         |                            |
| `cycleNumber`              | `Integer`        |                            |
| `closedSeaCover`           | `Integer`        |                            |
| `openOceanCover`           | `Integer`        |                            |
| `processingDate`           | `DateTimeOffset` |                            |
| `snowOrIceCover`           | `Double`         |                            |
| `lastOrbitNumber`          | `Integer`        |                            |
| `operationalMode`          | `String`         |                            |
| `processingLevel`          | `String`         |                            |
| `salineWaterCover`         | `Double`         |                            |
| `tidalRegionCover`         | `Double`         |                            |
| `baselineCollection`       | `String`         |                            |
| `lastOrbitDirection`       | `String`         |                            |
| `processingBaseline`       | `String`         |                            |
| `continentalIceCover`      | `Integer`        |                            |
| `freshInlandWaterCover`    | `Double`         |                            |
| `lastRelativeOrbitNumber`  | `Integer`        |                            |

## Sentinel-5P

| Name                       | Type             | STAC property 
|----------------------------|------------------|-----------------------|
| `platformShortName`        | `String`         | `constellation`       |
| `platformSerialIdentifier` | `String`         | `platform`            |
| `instrumentShortName`      | `String`         | `instruments`         |
| `productType`              | `String`         | `product:type`        |
| `orbitNumber`              | `Integer`        | `sat:absolute_orbit`  |
| `processorName`            | `String`         | `processing:software` |
| `processorVersion`         | `String`         | `processing:software` |
| `processingCenter`         | `String`         | `processing:facility` |
| `doi`                      | `String`         |                       |
| `identifier`               | `String`         |                       |
| `coordinates`              | `String`         |                       |
| `productClass`             | `String`         |                       |
| `qualityStatus`            | `String`         |                       |
| `processingDate`           | `DateTimeOffset` |                       |
| `processingMode`           | `String`         |                       |
| `acquisitionType`          | `String`         |                       |
| `processingLevel`          | `String`         |                       |
| `parentIdentifier`         | `String`         |                       |
| `baselineCollection`       | `String`         |                       |
| `processingBaseline`       | `String`         |                       |

## Additional Attributes

| Name                     | Type             |
|--------------------------|------------------|
| `Collection/Name`        | `String`         |
| `PublicationDate`        | `DateTimeOffset` |
| `ModificationDate`       | `DateTimeOffset` |
