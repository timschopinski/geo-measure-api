from math import sqrt, cos, radians, atan2, sin
from config.settings.common import EARTH_RADIUS
from gps.geo import Point


class DistanceCalculator:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def calculate(self) -> float:
        latitude_1, longitude_1 = self.point_1.coordinates
        latitude_2, longitude_2 = self.point_2.coordinates

        dlat = radians(latitude_2 - latitude_1)
        dlon = radians(longitude_2 - longitude_1)
        a = sin(dlat / 2)**2 + cos(radians(latitude_1)) * cos(radians(latitude_2)) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = EARTH_RADIUS * c

        return distance
