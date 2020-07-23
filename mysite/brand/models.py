from django.db import models

class City(models.Model):
    name=models.CharField(max_length=100,null=True)
    

class Person(models.Model):
    name=models.CharField(max_length=100,null=True)
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

class Book(models.Model):
    name=models.CharField(max_length=100,null=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)