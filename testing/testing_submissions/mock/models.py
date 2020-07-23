from django.db import models


class Party(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=100,default='JanaSena')