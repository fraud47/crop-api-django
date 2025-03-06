from rest_framework import serializers

from ...models import Farmer


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('owner', None)

        return representation
