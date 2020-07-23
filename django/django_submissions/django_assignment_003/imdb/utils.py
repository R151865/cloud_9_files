from imdb.models import *

def populate_database(actors_list=None, 
                        directors_list=None,
                        movies_list=None,
                        movie_rating_list=None):
                        
    if actors_list:
        for item in actors_list:
            actor=Actor.objects.create(
                actor_id=item['actor_id'],
                name=item['name'])
        
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
                          
def get_average_rating_of_movie(movie_obj):
    try:
        movie_rating=Rating.objects.get(movie=movie_obj)
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
        
def total_number_ratings(movie_obj):
    try:
        movie_rating=Rating.objects.get(movie=movie_obj)
        total_number=(movie_rating.rating_one_count+
            movie_rating.rating_two_count+
            movie_rating.rating_three_count+
            movie_rating.rating_four_count+
            movie_rating.rating_five_count)
        return total_number
    except :
        return 0
    
# 1                          
def get_movies_by_given_movie_names(movie_names):
    movie_details_in_dict=[]
    if len(movie_names)>0 and type(movie_names[0])==str :
        movies_list=Movie.objects.filter(name__in=movie_names)
    else:
        movies_list=movie_names

    for movie in movies_list:
        average_rating=get_average_rating_of_movie(movie)
        sum_of_rating=total_number_ratings(movie)
        cast_list=[]
        for casts in Cast.objects.filter(movie=movie):
            cast_dict={}
            actor_list={}
            actor_list={
                'name':casts.actor.name,
                'actor_id':casts.actor.actor_id
            }
            cast_dict={
                'actor':actor_list, 
                'role':casts.role,
                'is_debut_movie':casts.is_debut_movie
            }
            cast_list.append(cast_dict)
        
        movie_dict={}
        movie_dict={
            'movie_id':movie.movie_id,
            'name': movie.name,
            'cast':cast_list,
            "box_office_collection_in_crores":movie.box_office_collection_in_crores,
            "release_date":(movie.release_date).strftime("%Y-%m-%d"),
            "director_name":movie.director.name,
            "average_rating":average_rating,
            "total_number_of_ratings":sum_of_rating
        }
        movie_details_in_dict.append(movie_dict)
        
    return movie_details_in_dict
     
     
#need to modify it better    
def get_movies_released_in_summer_in_given_years():
    from django.db.models import Q
    movie_names=Movie.objects.filter(
        release_date__month__in=[5,6,7],
        release_date__year__gt=2005,
        release_date__year__lt=2010
        ).distinct()
        
    return get_movies_by_given_movie_names(movie_names)

    
def get_movie_names_with_actor_name_ending_with_smith():
    mov_list=Movie.objects.filter(actors__name__iendswith='smith').values_list('name',flat=True).distinct()
    return mov_list

#need to modify it to be better    
#task -4
def get_movie_names_with_ratings_in_given_range():
    from django.db.models import Q
    movie_lists=Movie.objects.filter(
        Q(rating__rating_five_count__gte=1000),
        Q(rating__rating_five_count__lte=3000)
        ).values_list('name',flat=True).distinct()
    
    return movie_lists

#task -5    
def get_movie_names_with_ratings_above_given_minimum():
    from django.db.models import Q
    movie_list=Movie.objects.filter(Q(rating__rating_five_count__gte=500)|
        Q(rating__rating_four_count__gte=1000)|
        Q(rating__rating_three_count__gte=2000)|
        Q(rating__rating_two_count__gte=4000)|
        Q(rating__rating_one_count__gte=8000),
        Q(release_date__year__gt=2000)
        ).values_list('name',flat=True).distinct()
    return movie_list

def get_movie_directors_in_given_year():
    dir_list=Director.objects.filter(movie__release_date__year=2000).values_list('name',flat=True).distinct()
    return dir_list

#task -7
def get_actor_names_debuted_in_21st_century():
    from django.db.models import Q
    actor_list=Actor.objects.filter(
        Q(movie__release_date__year__gt=2000),
        Q(movie__release_date__year__lte=2100),
        Q(cast__is_debut_movie=True)
        ).values_list('name',flat=True).distinct()
    return actor_list 
    

def get_director_names_containing_big_as_well_as_movie_in_may():
    from django.db.models import Q
    dir_list=Director.objects.filter(movie__name__contains='big').filter(
        Q(movie__release_date__month=5)).values_list('name',flat=True).distinct()
    return dir_list



def get_director_names_containing_big_and_movie_in_may():
    from django.db.models import Q
    dir_list=Director.objects.filter(
        Q(movie__release_date__month=5),Q(movie__name__contains='big')
        ).values_list('name',flat=True).distinct()
    return dir_list


def reset_ratings_for_movies_in_this_year():
    Rating.objects.filter(movie__release_date__year=2000).update(
        rating_one_count=0,
        rating_two_count=0,
        rating_three_count=0,
        rating_four_count=0,
        rating_five_count=0
        )
	
	