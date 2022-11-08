from django.db import models

# Create your models here.


class Model(models.Model):
    TYPES = [
        (1, 'Cordless'),
        (2, 'Robot'),
        (3, 'Wet Dry Vac'),
        (4, 'Upright'),
        (5, 'Canister')
    ]
    name = models.CharField(max_length=20, blank=False, unique=True)
    description = models.CharField(max_length=100)