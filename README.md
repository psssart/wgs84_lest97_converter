# My Coordinate Converter

This package provides functions to convert coordinates between WGS84 and L-Est97 systems using pyproj 3.7.1.

## Installation

Install with pip:

```pip install my_coord_converter```

## Usage

```python
from my_coord_converter import wgs84_to_est97, est97_to_wgs84

# Convert from WGS84 to L-Est97
x, y = wgs84_to_est97(24.7536, 59.43696)

# Convert from L-Est97 to WGS84
lon, lat = est97_to_wgs84(x, y)
