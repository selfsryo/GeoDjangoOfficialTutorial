from world.models import WorldBorder

from rest_framework_gis.serializers import GeoFeatureModelSerializer

class WorldBorderSerializer(GeoFeatureModelSerializer):
# class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = 'mpoly'
        auto_bbox = True
        fields = ('__all__')
