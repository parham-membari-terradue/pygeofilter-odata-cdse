# Supported attributes

As stated, this library was initially developed to support CDSE use cases only, so please make sure the parameters users can query.

## Sentinel-1

| Name                              | Type             |
|-----------------------------------|------------------|
| `productType`                     | `String`         |
| `origin`                          | `String`         |
| `datatakeID`                      | `Integer`        |
| `timeliness`                      | `String`         |
| `coordinates`                     | `String`         |
| `cycleNumber`                     | `Integer`        |
| `orbitNumber`                     | `Integer`        |
| `sliceNumber`                     | `Integer`        |
| `totalSlices`                     | `Integer`        |
| `productClass`                    | `String`         |
| `processorName`                   | `String`         |
| `orbitDirection`                  | `String`         |
| `processingDate`                  | `DateTimeOffset` |
| `operationalMode`                 | `String`         |
| `processingLevel`                 | `String`         |
| `swathIdentifier`                 | `String`         |
| `processingCenter`                | `String`         |
| `processorVersion`                | `String`         |
| `segmentStartTime`                | `DateTimeOffset` |
| `sliceProductFlag`                | `Boolean`        |
| `platformShortName`               | `String`         |
| `productGeneration`               | `DateTimeOffset` |
| `processingBaseline`              | `String`         |
| `productComposition`              | `String`         |
| `instrumentShortName`             | `String`         |
| `relativeOrbitNumber`             | `Integer`        |
| `polarisationChannels`            | `String`         |
| `productConsolidation`            | `String`         |
| `platformSerialIdentifier`        | `String`         |
| `instrumentConfigurationID`       | `Integer`        |
| `startTimeFromAscendingNode`      | `Double`         |
| `completionTimeFromAscendingNode` | `Double`         |

## Sentinel-1-RTC

| Name                       | Type      |
|----------------------------|-----------|
| `productType`              | `String`  |
| `authority`                | `String`  |
| `orbitNumber`              | `Integer` |
| `orbitDirection`           | `String`  |
| `operationalMode`          | `String`  |
| `processingLevel`          | `String`  |
| `platformShortName`        | `String`  |
| `spatialResolution`        | `Integer` |
| `instrumentShortName`      | `String`  |
| `relativeOrbitNumber`      | `Integer` |
| `polarisationChannels`     | `String`  |
| `platformSerialIdentifier` | `String`  |

## Sentinel-2

| Name                       | Type             |
|----------------------------|------------------|
| `productType`              | `String`         |
| `origin`                   | `String`         |
| `tileId`                   | `String`         |
| `cloudCover`               | `Double`         |
| `coordinates`              | `String`         |
| `datastripId`              | `String`         |
| `orbitNumber`              | `Integer`        |
| `qualityInfo`              | `Integer`        |
| `qualityStatus`            | `String`         |
| `sourceProduct`            | `String`         |
| `processingDate`           | `DateTimeOffset` |
| `productGroupId`           | `String`         |
| `lastOrbitNumber`          | `Integer`        |
| `operationalMode`          | `String`         |
| `processingLevel`          | `String`         |
| `processingCenter`         | `String`         |
| `processorVersion`         | `String`         |
| `granuleIdentifier`        | `String`         |
| `platformShortName`        | `String`         |
| `processingBaseline`       | `String`         |
| `instrumentShortName`      | `String`         |
| `relativeOrbitNumber`      | `Integer`        |
| `illuminationZenithAngle`  | `Double`         |
| `sourceProductOriginDate`  | `String`         |
| `platformSerialIdentifier` | `String`         |

## Sentinel-3

| Name                       | Type             |
|----------------------------|------------------|
| `productType`              | `String`         |
| `landCover`                | `Double`         |
| `cloudCover`               | `Double`         |
| `timeliness`               | `String`         |
| `brightCover`              | `Double`         |
| `coordinates`              | `String`         |
| `cycleNumber`              | `Integer`        |
| `orbitNumber`              | `Integer`        |
| `coastalCover`             | `Double`         |
| `processorName`            | `String`         |
| `closedSeaCover`           | `Integer`        |
| `openOceanCover`           | `Integer`        |
| `orbitDirection`           | `String`         |
| `processingDate`           | `DateTimeOffset` |
| `snowOrIceCover`           | `Double`         |
| `lastOrbitNumber`          | `Integer`        |
| `operationalMode`          | `String`         |
| `processingLevel`          | `String`         |
| `processingCenter`         | `String`         |
| `processorVersion`         | `String`         |
| `salineWaterCover`         | `Double`         |
| `tidalRegionCover`         | `Double`         |
| `platformShortName`        | `String`         |
| `baselineCollection`       | `String`         |
| `lastOrbitDirection`       | `String`         |
| `processingBaseline`       | `String`         |
| `continentalIceCover`      | `Integer`        |
| `instrumentShortName`      | `String`         |
| `relativeOrbitNumber`      | `Integer`        |
| `freshInlandWaterCover`    | `Double`         |
| `lastRelativeOrbitNumber`  | `Integer`        |
| `platformSerialIdentifier` | `String`         |

## Sentinel-5P

| Name                       | Type             |
|----------------------------|------------------|
| `productType`             | `String`         |
| `doi`                      | `String`          |
| `identifier`               | `String`         |
| `coordinates`              | `String`         |
| `orbitNumber`              | `Integer`        |
| `productClass`             | `String`         |
| `processorName`            | `String`         |
| `qualityStatus`            | `String`         |
| `processingDate`           | `DateTimeOffset` |
| `processingMode`           | `String`         |
| `acquisitionType`          | `String`         |
| `processingLevel`          | `String`         |
| `parentIdentifier`         | `String`         |
| `processingCenter`         | `String`         |
| `processorVersion`         | `String`         |
| `platformShortName`        | `String`         |
| `baselineCollection`       | `String`         |
| `processingBaseline`       | `String`         |
| `instrumentShortName`      | `String`         |
| `platformSerialIdentifier` | `String`         |

## Additional Attributes

| Name                       | Type             |
|----------------------------|------------------|
| `Collection/Name`        | `String`         |
| `PublicationDate`        | `DateTimeOffset` |
| `ModificationDate`       | `DateTimeOffset` |
