from imdb.models import *
from django.db.models import Q,Count
from collections import defaultdict

def get_average_rating_of_movie(movie_obj):
    try:
        movie_rating=movie_obj.rating
        numb=(  movie_rating.rating_one_count+
                movie_rating.rating_two_count+
                movie_rating.rating_three_count+
                movie_rating.rating_four_count+
                movie_rating.rating_five_count
             )

        average=( movie_rating.rating_one_count*1+
                  movie_rating.rating_two_count*2+
                  movie_rating.rating_three_count*3+
                  movie_rating.rating_four_count*4+
                  movie_rating.rating_five_count*5
                )*1.0/numb
                
        return average
    except :
        return 0  
        
def total_number_ratings(movie_obj):
    try:
        movie_rating=movie_obj.rating
        total_number=(  movie_rating.rating_one_count+
                        movie_rating.rating_two_count+
                        movie_rating.rating_three_count+
                        movie_rating.rating_four_count+
                        movie_rating.rating_five_count
                     )
        return total_number
    except :
        return 0
    

#1
def populate_database(  actors_list=None,
                        movies_list=None,
                        directors_list=None,
                        movie_rating_list=None
                      ):
                          
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
            bulk_directors_list.append( Director(name=director) )
            
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
def get_movies_by_given_movie_names(movie_names=None,FEMALE=False):
    
    if FEMALE:
        f_count=Count('actors',filter=Q(actors__gender='FEMALE')) 
        cast_list=Cast.objects.select_related('actor','movie__rating','movie__director').filter(
            movie__in=Movie.objects.annotate(f_count=f_count).filter(f_count__gt=5)).filter(actor__gender='FEMALE')
    else:
        cast_list=Cast.objects.select_related('actor','movie__rating','movie__director').filter(movie__name__in=movie_names)
    
    cast_dict=defaultdict(list)
    for cast in cast_list:
        cast_dict[cast.movie].append(cast)
    movie_details=[]
    for movie,casts in cast_dict.items():
        cast_list=[]
        for  cast_item in casts:
            actor={}
            cast_details={}
            actor['name']=cast_item.actor.name
            actor['actor_id']=cast_item.actor.actor_id
            cast_details['actor']=actor
            cast_details['role']=cast_item.role
            cast_details['is_debut_movie']=cast_item.is_debut_movie
            cast_list.append(cast_details)
                
        mov_dict={
                    'movie_id':movie.movie_id,
                    'name':movie.name,
                    'cast':cast_list,
                    'box_office_collection_in_crores':movie.box_office_collection_in_crores,
                    'release_date':str(movie.release_date),
                    'director_name':movie.director.name,
                    'average_rating':get_average_rating_of_movie(movie),
                    'total_number_of_ratings':total_number_ratings(movie)
                }
        movie_details.append(mov_dict)
    return movie_details
    
        
#5
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    return list(Actor.objects.filter(movie__in=movie_objs).distinct())

#6
def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    return get_movies_by_given_movie_names(FEMALE=True)
    
#7
def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    #NEED TO CHANGE THE YEAR 2000
    cast_list=Cast.objects.select_related('actor','movie__rating','movie__director').filter(movie__release_date__year__gte=2000)  
    
    cast_dict=defaultdict(dict)
    for cast in cast_list:
        actor_dict=cast_dict[cast.actor]
        actor_dict[cast.movie]=actor_dict.get(cast.movie,[])
        cast_dict[cast.actor]=actor_dict
        cast_dict[cast.actor][cast.movie].append(cast)
            
    
    actor_movies_details=[]
    for actor,movies in cast_dict.items():
        movies_list=[]
        for movie,casts in movies.items():
            cast_list=[]
            for actor_role in casts:
                
                casts_dictionary={
                                'role':actor_role.role,
                                'is_debut_movie':actor_role.is_debut_movie
                              }
                cast_list.append(casts_dictionary)
            
            mov_dict={
                            'movie_id':movie.movie_id,
                            'name':movie.name,
                            'cast':cast_list,
                            'box_office_collection_in_crores':movie.box_office_collection_in_crores,
                            'release_date':str(movie.release_date),
                            'director_name':movie.director.name,
                            'average_rating':get_average_rating_of_movie(movie),
                            'total_number_of_ratings':total_number_ratings(movie)
                        }
            movies_list.append(mov_dict)
            
        actor_and_his_movies={
                                'name':actor.name,
                                'actor_id':actor.actor_id,
                                'movies':movies_list
                                }
        actor_movies_details.append(actor_and_his_movies)    
    return  actor_movies_details 
    
        
    
#8
def reset_ratings_for_movies_in_given_year(year):
    Rating.objects.filter(movie__release_date__year=year).update(
                                                                    rating_one_count=0,
                                                                    rating_two_count=0,
                                                                    rating_three_count=0,
                                                                    rating_four_count=0,
                                                                    rating_five_count=0
                                                                    )
    