# main/converter.py

from pyproj import Transformer

# Transformer for converting from WGS84 to L-Est97 (EPSG:4326 to EPSG:3301)
transformer_to_est97 = Transformer.from_crs("EPSG:4326", "EPSG:3301", always_xy=True)
# Transformer for converting from L-Est97 to WGS84 (EPSG:3301 to EPSG:4326)
transformer_to_wgs84 = Transformer.from_crs("EPSG:3301", "EPSG:4326", always_xy=True)


def wgs84_to_est97(lon, lat):
    """
    Convert coordinates from WGS84 to L-Est97.

    :param lon: Longitude in WGS84
    :param lat: Latitude in WGS84
    :return: Tuple (x, y) in L-Est97
    """
    x, y = transformer_to_est97.transform(lon, lat)
    return x, y


def est97_to_wgs84(x, y):
    """
    Convert coordinates from L-Est97 to WGS84.

    :param x: X coordinate in L-Est97
    :param y: Y coordinate in L-Est97
    :return: Tuple (lon, lat) in WGS84
    """
    lon, lat = transformer_to_wgs84.transform(x, y)
    return lon, lat
