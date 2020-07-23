from app1.models import *

def pop():
    blog_list=[
        {
            'name':'blog 1',
            'tagline':'tagline 1'
        },
        {
            'name':'blog 2',
            'tagline':'tagline 2'
        }
        ]
    
    
    author_list=[
        {
            'name':'author 1'
        },
        {
            'name':'author 2'
        },
        
        ]
        
    entry_list=[
        {
            'headline':'entry headline 1',
            'pub_date':'2000-10-10',
            'author':'author 1',
            'blog':'blog 1'
        },
        {
            'headline':'entry headline 2',
            'pub_date':'2005-10-10',
            'author':'author 1',
            'blog':'blog 2'
        }
        ]
    
    ed_list=[
        {
         'entry':'headline 1',
         'details':'details 1'
        }
        ]
        
    for blog in blog_list:
        Blog.objects.create(
            name=blog['name'],
            tagline=blog['tagline'])
            
    for author in author_list:
        Author.objects.create(
            name=author['name'],
            )
    for entry in entry_list:
        bl=Blog.objects.filter(name=entry['blog'])[0]
        Entry.objects.create(
            headline=entry['headline'],
            pub_date=entry['pub_date'],
            blog=bl
            )
    
            