from imdb.models import *
from django.db.models import Q,Avg,Count,Max,Min,Prefetch

def get_average_rating_of_movie(rating_obj):
    try:
        movie_rating=rating_obj
        numb=(movie_rating.rating_one_count+
            movie_rating.rating_two_count+
            movie_rating.rating_three_count+
            movie_rating.rating_four_count+
            movie_rating.rating_five_count)

        average=(movie_rating.rating_one_count*1+
            movie_rating.rating_two_count*2+
            movie_rating.rating_three_count*3+
            movie_rating.rating_four_count*4+
            movie_rating.rating_five_count*5)*1.0/numb
            
        return average
    except :
        return 0  
        
def total_number_ratings(rating_obj):
    try:
        movie_rating=rating_obj
        total_number=(movie_rating.rating_one_count+
            movie_rating.rating_two_count+
            movie_rating.rating_three_count+
            movie_rating.rating_four_count+
            movie_rating.rating_five_count)
        return total_number
    except :
        return 0
    





#1
def populate_database(actors_list=None,
                    movies_list=None,
                    directors_list=None,
                    movie_rating_list=None):
    if actors_list:
        bulk_actors_list=[]
        for actor in actors_list:
            bulk_actors_list.append(
                Actor(actor_id=actor['actor_id'],
                name=actor['name'],
                gender=actor['gender'])
                )
        Actor.objects.bulk_create(bulk_actors_list)
        
    if directors_list:    
        bulk_directors_list=[]
        for director in directors_list:
            bulk_directors_list.append(
                Director(name=director)
                )
        Director.objects.bulk_create(bulk_directors_list)
    
    if movies_list:
        bulk_movies_list=[]
        dir_list=Director.objects.all()
        for movie in movies_list:
            
            dir_inst=0
            for i in dir_list:
                if i.name==movie['director_name']:
                    dir_inst=i
                    
            bulk_movies_list.append(
                Movie(
                    movie_id=movie['movie_id'],
                    name=movie['name'],
                    box_office_collection_in_crores=movie['box_office_collection_in_crores'],
                    release_date=movie['release_date'],
                    director_id=dir_inst.id
                    )
                )
        Movie.objects.bulk_create(bulk_movies_list)
        bulk_casts_list=[]
        for movie in movies_list:
            for cast_item in movie['actors']:
                bulk_casts_list.append(
                    Cast(
                        movie_id=movie['movie_id'],
                        actor_id=cast_item['actor_id'],
                        role=cast_item['role'],
                        is_debut_movie=cast_item['is_debut_movie']
                        )
                )
        Cast.objects.bulk_create(bulk_casts_list)
                
    
    if movie_rating_list:
        bulk_rating_list=[]
        for rating in movie_rating_list:
            bulk_rating_list.append(
                Rating(
                    movie_id=rating['movie_id'],
                    rating_one_count=rating['rating_one_count'],
                    rating_two_count=rating['rating_two_count'],
                    rating_three_count=rating['rating_three_count'],
                    rating_four_count=rating['rating_four_count'],
                    rating_five_count=rating['rating_five_count']
                    )
                )
        Rating.objects.bulk_create(bulk_rating_list)
    
    
#2
def remove_all_actors_from_given_movie(movie_object):
    movie_object.actors.clear()


#3
def get_all_rating_objects_for_given_movies(movie_objs):
    return list(Rating.objects.filter(movie_id__in=movie_objs))
  
  
#4
def get_movies_by_given_movie_names(movie_names):
    # movies, cast,director, average_rating,total number of rating
    
    if movie_names and movie_names[]
    
    mov_list=Movie.objects.filter(name__in=movie_names).select_related(
        'director','rating').prefetch_related('cast_set__actor')
        
    movie_details_in_list=[]
    for movie in mov_list:
        
        try:
            average=get_average_rating_of_movie(movie.rating)
            total=total_number_ratings(movie.rating)
        except:
            average=0
            total=0
            
        
        cast_list=[]
        for casts in movie.cast_set.all():
            actors_dict={
                'actor':{
                    'name':casts.actor.name,
                    'actor_id':casts.actor.actor_id
                },
                'role':casts.role,
                'is_debut_movie':casts.is_debut_movie
            }
            cast_list.append(actors_dict)
            
        mov_dict={
        'movie_id':movie.movie_id,
        'name':movie.name,
        'cast':cast_list,
        'box_office_collection_in_crores':movie.box_office_collection_in_crores,
        'release_date':str(movie.release_date),
        'director_name':movie.director.name,
        'average_rating':average,
        'total_number_ratings':total
        
        }
        
        movie_details_in_list.append(mov_dict)
        
    return movie_details_in_list
        
    
            
    
    """
    :movie_names: list of strings
    :return:
    [{
        "movie_id": 1,
        "name": "Titanic",
        "cast": [
            {
                "actor": {
                    "name": "Kate Winslet",
                    "actor_id": 1
                },
                "role": "Lead Actress",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "218.7",
        "release_date": "1997-11-18",
        "director_name": "James Cameron",
        "average_rating": 4.9,
        "total_number_of_ratings": 1000
    }]
    """
    

#5
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    return list(Actor.objects.filter(movie__movie_id__in=movie_objs).distinct())

#6
def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    #need to change the female coutn
    
    female_count=Count('actors',distinct=True,filter=Q(actors__gender='FEMALE'))
    mov_list=Movie.objects.prefetch_related('actors').annotate(
        female_count=female_count).filter(female_count__gt=5)
    
    return get_movies_by_given_movie_names(mov_list)
    
    
    
  """
  :return:
    [{
        "movie_id": 1,
        "name": "Titanic",
        "cast": [
            {
                "actor": {
                    "name": "Kate Winslet",
                    "actor_id": 1
                },
                "role": "Lead Actress",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "218.7",
        "release_date": "1997-11-18",
        "director_name": "James Cameron",
        "average_rating": 4.9,
        "total_number_of_ratings": 1000
    }]
  """

    


#8
def reset_ratings_for_movies_in_given_year(year):
    Rating.objects.filter(movie__release_date__year=year).update(
        rating_one_count=0,
        rating_two_count=0,
        rating_three_count=0,
        rating_four_count=0,
        rating_five_count=0
        )
    