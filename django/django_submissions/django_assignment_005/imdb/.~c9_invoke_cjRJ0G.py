from imdb.models import *

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
    movie_names=['movie_1','movie_2']
    
    Prefetch('actors')
    Prefetch('cast')
    mov_list=Movie.objects.prefetch_related(
        Prefetch('actors'),
        Prefetch('cast')
        )
    
    
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