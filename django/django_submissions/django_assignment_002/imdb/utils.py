from imdb.models import *
from datetime import date
from django.core.exceptions import ObjectDoesNotExist


def populate_database(actors_list=None, movies_list=None, directors_list=None, movie_rating_list=None):
                        
    if actors_list:
        for item in actors_list:
            actor=Actor.objects.create(actor_id=item['actor_id'],name=item['name'])
        
    if directors_list:    
        for item in directors_list:
            Director.objects.create(name=item)
    
    #doubt in movie
    if movies_list:
        for item in movies_list:
            movie=Movie.objects.create(
                movie_id=item['movie_id'],
                name=item['name'],
                box_office_collection_in_crores=item[ "box_office_collection_in_crores"],
                release_date=item['release_date'],
                director=Director.objects.get(pk=item['director_name'])
            )
            for cast_item in item['actors']:
                cast=Cast.objects.create(
                    actor=Actor.objects.get(pk=cast_item['actor_id']),
                    movie=Movie.objects.get(pk=item['movie_id']),
                    role=cast_item['role'],
                    is_debut_movie=cast_item['is_debut_movie']
                )
                    
                
    if movie_rating_list:  
        for item in movie_rating_list:
            rating=Rating.objects.create(
                movie=Movie.objects.get(pk=item['movie_id']),
                rating_one_count=item['rating_one_count'],
                rating_two_count=item['rating_two_count'],
                rating_three_count=item['rating_three_count'],
                rating_four_count=item['rating_four_count'],
                rating_five_count=item['rating_five_count']
            )
                                          
                                    
def get_no_of_distinct_movies_actor_acted(actor_id):
  return Actor.objects.get(actor_id=actor_id).movie_set.all().distinct().count()

    
def get_movies_directed_by_director(director_obj):
    return director_obj.movie_set.all()

#need less code i have seeee it again to reduce the code
def get_average_rating_of_movie(movie_obj):
    try:
        movie_rating=movie_obj.rating
    
    except :
        return 0
        
    average=(movie_rating.rating_one_count*1+
        movie_rating.rating_two_count*2+
        movie_rating.rating_three_count*3+
        movie_rating.rating_four_count*4+
        movie_rating.rating_five_count*5)*1.0/5
    return average
    
    
def delete_movie_rating(movie_obj):
    Rating.objects.filter(movie_id=movie_obj).delete()
    return 


def get_all_actor_objects_acted_in_given_movies(movie_objs):
   return Actor.objects.filter(movie__in=movie_objs).distinct()
 
    
def update_director_for_given_movie(movie_obj, director_obj):
    movie_obj.director=director_obj
    movie_obj.save()
    return 
    
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    return Movie.objects.filter(actors__name__contains='john').distinct()
    
def remove_all_actors_from_given_movie(movie_obj):
    movie_obj.actors.clear()
    return 
   
def get_all_rating_objects_for_given_movies(movie_objs):
    return(Rating.objects.filter(movie_id__in=movie_objs))

  