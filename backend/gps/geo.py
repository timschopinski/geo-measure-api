

class Point:
    def __init__(self, longitude: float, latitude: float):
        self.longitude = longitude
        self.latitude = latitude

    @property
    def coordinates(self) -> tuple[float, float]:
        return self.longitude, self.latitude
