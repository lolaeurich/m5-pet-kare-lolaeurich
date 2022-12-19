from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from groups.models import Group
from pets.models import Pet
from pets.serializers import PetSerializer
from traits.models import Trait


class PetView(APIView):
    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        group_data = serializer.validated_data.pop('group')
        traits_data = serializer.validated_data.pop('traits')

        group = Group.objects.get_or_create(**group_data)[0]

        pet = Pet.objects.create(**serializer.validated_data, group=group)

        for t in traits_data:
            trait = Trait.objects.get_or_create(**t)[0]
            trait.pet.add(pet)

        pet = PetSerializer(pet)
        return Response(pet.data, status=status.HTTP_201_CREATED)


class PetParamView(APIView):
    def get(self, request, pet_id=''):
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    def patch(self, request, pet_id=''):
        data_to_update = request.data
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet, data_to_update)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        updated_pet = serializer.save()
        serializer = PetSerializer(updated_pet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pet_id=''):
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
