from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from gps.geo import Point
from gps.serializers import DistanceSerializer, PolygonSerializer
from gps.tools import DistanceCalculator, AreaCalculator


class CalculateDistanceView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DistanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        point_1 = Point(**serializer.data['point_1'])
        point_2 = Point(**serializer.data['point_2'])
        distance_calculator = DistanceCalculator(point_1, point_2)
        distance = distance_calculator.calculate()

        return Response({'distance_m': distance}, status=status.HTTP_200_OK)


class CalculateAreaView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PolygonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        points = [Point(**point) for point in serializer.data['points']]

        try:
            area_calculator = AreaCalculator(points)
            area = area_calculator.calculate()
            return Response({'area_sq_m': area}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
