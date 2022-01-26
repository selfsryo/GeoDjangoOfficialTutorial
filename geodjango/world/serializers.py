from rest_framework import serializers

from world.models import WorldBorder


class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder
        fields = ('__all__')
