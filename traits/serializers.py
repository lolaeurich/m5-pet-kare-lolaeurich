from rest_framework import serializers

from traits.models import Trait


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_at = serializers.DateField(read_only=True)

    def create(self, validated_data: dict):
        return Trait.objects.create(**validated_data)
