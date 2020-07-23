from imdb.models import *
from django.db.models import Avg,Count,Max,Min,Count,Sum,Q

def populate_database(actors_list=[], 
                        directors_list=[],
                        movies_list=[],
                        movie_rating_list=[]):
                        
    if actors_list:
        for item in actors_list:
            actor=Actor.objects.create(
                actor_id=item['actor_id'],
                name=item['name'],
                gender=item['gender'])
        
    if directors_list:    
        for item in directors_list:
            Director.objects.create(name=item)
    
    if movies_list:
        for item in movies_list:
            
            movie=Movie.objects.create(
                name=item['name'],
                movie_id=item['movie_id'],
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
                          

#1
def get_average_box_office_collections():
    mov_list=Movie.objects.all()
    if mov_list.exists():
        avg=mov_list.aggregate(mov_average=Avg('box_office_collection_in_crores'))
        avg=round(avg['mov_average'],3)
        return avg
    else:
        return 0
    
  

#2
def get_movies_with_distinct_actors_count():
    return Movie.objects.all().annotate(actors_count=Count('actors',distinct=True))
    

#3
def get_male_and_female_actors_count_for_each_movie():
    male_actors_count =Count('actors',distinct=True,filter=Q(actors__gender='MALE'))
    female_actors_count=Count('actors',distinct=True,filter=Q(actors__gender='FEMALE'))
    
    mov_list=Movie.objects.annotate(
        male_actors_count=male_actors_count,
        female_actors_count=female_actors_count
        )
    return mov_list
    
#4

def get_roles_count_for_each_movie():
    return list(Movie.objects.annotate(roles_count=Count('cast__role',distinct=True)))
    
    
#5 
def get_role_frequency():
    cast_list=Cast.objects.values('role').annotate(dist_act_count=Count('actor',distinct=True))
    cast_dict={}
    
    for item in cast_list:
        cast_dict[item['role']]=item['dist_act_count']
    return cast_dict
        

#6

def get_role_frequency_in_order():
    return Cast.objects.values_list('role').annotate(count=Count('actor',distinct=True)).order_by('-movie__release_date')
    
#7
def get_no_of_movies_and_distinct_roles_for_each_actor():
    movies_count=Count('movie',distinct=True)
    roles_count=Count('cast__role',distinct=True)
    
    actors_list=Actor.objects.all().annotate(
        movies_count=movies_count,
        roles_count=roles_count)
    
    return list(actors_list)
    
#8
def get_movies_with_atleast_forty_actors():
    return Movie.objects.all().annotate(
        actors_count=Count('actors',distinct=True)).filter(actors_count__gte=40)
    
#9
def get_average_no_of_actors_for_all_movies():
    mov_list=Movie.objects.all()
    if mov_list.exists():
        avg=mov_list.annotate(
            actors_count=Count('actors',distinct=True)).aggregate(average=Avg('actors_count'))
        return round(avg['average'],3)
        
    else:
        return 0
    
    
   