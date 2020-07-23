from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100,null=True)
    tagline = models.TextField(null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True)
    headline = models.CharField(max_length=255,null=True)
    body_text = models.TextField(null=True)
    pub_date = models.DateField(null=True)
    mod_date = models.DateField(null=True)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(null=True)
    number_of_pingbacks = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.headline
        
class EntryDetails(models.Model):
    entry=models.OneToOneField(Entry,on_delete=models.CASCADE,null=True)
    details=models.TextField(null=True)
        


        
        
class S(models.Model):
    name=models.CharField(max_length=100,null=True)
    
    
class Question(models.Model):
    question=models.CharField(max_length=200,null=True)
    pub_date=models.DateTimeField('date published',null=True)
    
