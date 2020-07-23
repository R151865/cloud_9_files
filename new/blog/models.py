from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)

class Publisher(models.Model):
    name = models.CharField(max_length=300,null=True)

class Book(models.Model):
    name = models.CharField(max_length=300,null=True)
    pages = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    rating = models.FloatField(null=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,null=True)
    pubdate = models.DateField(null=True)

class Store(models.Model):
    name = models.CharField(max_length=300,null=True)
    books = models.ManyToManyField(Book)


class Sb(models.Model):
    name = models.CharField(max_length=300,null=True)
    books = models.ManyToManyField(Book)