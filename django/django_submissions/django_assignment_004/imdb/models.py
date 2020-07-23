from django.db import models
from datetime import date
# Create your models here.
#imdb model

class Actor(models.Model):
    actor_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Director(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.name


class Movie(models.Model):
    name=models.CharField(max_length=100)
    movie_id=models.CharField(max_length=100,primary_key=True)
    release_date=models.DateField()
    box_office_collection_in_crores=models.FloatField()
    actors=models.ManyToManyField(Actor,through='Cast')
    director=models.ForeignKey(Director,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Cast(models.Model):
    actor=models.ForeignKey(Actor,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    role=models.CharField(max_length=50)
    is_debut_movie=models.BooleanField(default=False)
    
    

class Rating(models.Model):
    movie=models.OneToOneField(Movie,on_delete=models.CASCADE)
    rating_one_count=models.IntegerField(default=0)
    rating_two_count=models.IntegerField(default=0)
    rating_three_count=models.IntegerField(default=0)
    rating_four_count=models.IntegerField(default=0)
    rating_five_count=models.IntegerField(default=0)
    
    




"""

actors_list=[
        {
            "actor_id": "actor_4",
            "name": "Actor 4",
            "gender": "MALE"
        },
        {
            "actor_id": "actor_5",
            "name": "Actor 5",
            "gender": "FEMALE"
        },
        {
            "actor_id": "actor_6",
            "name": "Actor 6",
            "gender": "MALE"
        },
        {
            "actor_id": "actor_7",
            "name": "Actor 7",
            "gender": "FEMALE"
        },
         {
            "actor_id": "actor_8",
            "name": "Actor 8",
            "gender": "FEMALE"
        }
        
    ]
    

movies_list=[
        {
            "movie_id": "movie_2",
            "name": "Movie 2",
            "actors": [
                {
                    "actor_id": "actor_1",
                    "role": "vilan",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_2",
                    "role": "vilan",
                    "is_debut_movie": True
                },
                {
                    "actor_id": "actor_3",
                    "role": "actress",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_3",
                    "role": "heroine",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_4",
                    "role": "side actor",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_6",
                    "role": "side actor",
                    "is_debut_movie": False
                }
            ],
            "box_office_collection_in_crores": "10",
            "release_date": "2020-3-3",
            "director_name": "Director 2"
        },
        {
            "movie_id": "movie_3",
            "name": "Movie 3",
            "actors": [
                {
                    "actor_id": "actor_8",
                    "role": "vilan",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_7",
                    "role": "vilan",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_3",
                    "role": "actress",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_4",
                    "role": "side actor",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_6",
                    "role": "side actor",
                    "is_debut_movie": False
                }
            ],
            "box_office_collection_in_crores": "20",
            "release_date": "2020-3-3",
            "director_name": "Director 3"
        },
        {
            "movie_id": "movie_4",
            "name": "Movie 4",
            "actors": [
                {
                    "actor_id": "actor_8",
                    "role": "vilan",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_7",
                    "role": "vilan",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_3",
                    "role": "actress",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_4",
                    "role": "side actor",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "actor_6",
                    "role": "side actor",
                    "is_debut_movie": False
                }
            ],
            "box_office_collection_in_crores": "21",
            "release_date": "2005-3-3",
            "director_name": "Director 1"
        }
    
    
    ]
    
directors_list=[
        "Director 6","Director 7","Director 8"
    ]
    
movie_rating_list= [
        
        {
            "movie_id": "movie_2",
            "rating_one_count": 4,
            "rating_two_count": 5,
            "rating_three_count": 4,
            "rating_four_count": 6,
            "rating_five_count": 7
        },
        {
            "movie_id": "movie_3",
            "rating_one_count": 4,
            "rating_two_count": 5,
            "rating_three_count": 4,
            "rating_four_count": 6,
            "rating_five_count": 7
        }
    ]


populate_database(actors_list=actors_list,
                movies_list=movies_list,
                directors_list=directors_list,
                movie_rating_list=movie_rating_list
                )
                

m=Movie.objects.filter(name='qw')
a=m.annotate(actors_count=Count('actors',distinct=True))
    








movies_list=[
        {
            "movie_id": "movie_5",
            "name": "Movie 5",
            "actors": [],
            "box_office_collection_in_crores": "30",
            "release_date": "2000-3-3",
            "director_name": "Director 7"
        }
        ]
populate_database(movies_list=movies_list)


"""
