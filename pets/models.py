from django.db import models
from groups.models import Group


class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
