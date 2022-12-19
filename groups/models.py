from django.db import models


class Group(models.Model):
    scientific_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
