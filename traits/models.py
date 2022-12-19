from django.db import models
from pets.models import Pet


class Trait(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    pet = models.ManyToManyField(Pet, related_name='traits')
