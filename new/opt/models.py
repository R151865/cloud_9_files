from django.db import models
import uuid
"""
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender =  models.CharField(max_length=10, choices=[
        ('M','M'),('F','F')])

"""








"""
class Library(models.Model):
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    
class Author(models.Model):
    name = models.CharField(max_length=200, default='')

class Book(models.Model):
    library = models.ForeignKey(Library,on_delete=models.CASCADE,
    related_name='books',
    )
    author = models.ForeignKey(Author,on_delete=models.CASCADE,
        related_name='books'
    )
    
    title = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')

    def get_page_count(self):
        return self.pages.count()

class Page(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='pages',
    )
    text = models.TextField(null=True, blank=True)
    page_number = models.IntegerField()
    
    
    
    
    

class City1(models.Model):
    name=models.CharField(max_length=100,null=True)
    

class Person1(models.Model):
    name=models.CharField(max_length=100,null=True)
    hometown = models.ForeignKey(
        City1,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

class Book1(models.Model):
    name=models.CharField(max_length=100,null=True)
    author = models.ForeignKey(Person1, on_delete=models.CASCADE)
    
# prefetch-related

class Topping(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Pizza(models.Model):
    vegetarian=models.BooleanField(default=False,null=True)
    spicy=models.BooleanField(default=True,null=True)
    
    name=models.CharField(max_length=50)
    toppings=models.ManyToManyField(Topping)
   
    
    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )
class Restaurant(models.Model):
    
    
    pizzas=models.ManyToManyField(Pizza,
    related_name='restaurants')
    
    best_pizza=models.ForeignKey(Pizza,
    related_name='championed_by',
    on_delete=models.CASCADE)
    
    
class P(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField(default=10)
    
class Rep(models.Model):
    stories_filed=models.IntegerField()
    no_of_badges=models.IntegerField()
    
    
#products order orderproducts
class Club(models.Model):
    name=models.CharField(max_length=100)
    
class Player(models.Model):
    player_id=models.UUIDField()
    club=models.ForeignKey(Club,on_delete=models.CASCADE)

class Cage(models.Model):
    clubs=models.ManyToManyField(Club)
"""