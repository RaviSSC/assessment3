from django.db import models

# Create your models here.
class Plane(models.Model):
    name=models.TextField(max_length=255)
