from rest_framework import serializers

from groups.models import Group
from groups.serializers import GroupSerializer
from traits.models import Trait
from traits.serializers import TraitSerializer

from pets.models import Pet


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def create(self, validated_data: dict):
        group_data = validated_data.pop('group')
        traits_data = validated_data.pop('traits')

        group = Group.objects.get_or_create(**group_data)[0]

        pet = Pet.objects.create(**validated_data, group=group)

        for t in traits_data:
            trait = Trait.objects.get_or_create(**t)[0]
            trait.pet.add(pet)
        return pet

    def update (self, instance: Pet, validated_data: dict):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.weight = validated_data.get("weight", instance.weight)
        instance.sex = validated_data.get("sex", instance.sex)

        group_name = validated_data.get("group")['scientific_name']
        group = Group.objects.get_or_create(scientific_name=group_name)[0]
        instance.group = group

        traits = validated_data.get("traits")
        new_traits = []

        for t in traits:
            trait = Trait.objects.get_or_create(name=t['name'])[0]
            new_traits.append(trait)

        instance.traits.set(new_traits)

        instance.save()
        return instance
