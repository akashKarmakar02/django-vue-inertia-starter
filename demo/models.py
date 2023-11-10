from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=255)
    girlfriend = models.CharField(max_length=255)
