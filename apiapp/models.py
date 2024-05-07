from django.db import models

class ApiTestModel(models.Model):
    title = models.CharField(max_length=255)
    # Create your models here.
