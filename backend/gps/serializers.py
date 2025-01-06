from rest_framework import serializers


class PointSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    class Meta:
        fields = ('latitude', 'longitude')


class DistanceSerializer(serializers.Serializer):
    point_1 = PointSerializer()
    point_2 = PointSerializer()

    class Meta:
        fields = ('point_1', 'point_2')


class PolygonSerializer(serializers.Serializer):
    points = PointSerializer(many=True, min_length=3, help_text='List of points representing the polygon vertices.')

    class Meta:
        fields = ('points',)
