from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework_gis.pagination import GeoJsonPagination
from world.serializers import WorldBorderSerializer
from world.models import WorldBorder


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
    pagination_class = MyPagination
    # page_size_query_param = 'page_size'
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'mpoly'
    distance_filter_convert_meters = True