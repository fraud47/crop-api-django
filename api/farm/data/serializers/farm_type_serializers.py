from rest_framework import serializers
from ...models.farm_type import FarmType

class FarmTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmType
        fields = '__all__'
