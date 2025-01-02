from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from gps.geo import Point
from gps.serializers import DistanceSerializer
from gps.tools import DistanceCalculator


class CalculateDistanceView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DistanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        point_1 = Point(**serializer.data['point_1'])
        point_2 = Point(**serializer.data['point_2'])
        distance_calculator = DistanceCalculator(point_1, point_2)
        distance = distance_calculator.calculate()

        return Response({'distance_km': distance}, status=status.HTTP_200_OK)
