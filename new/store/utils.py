from store.models import *

def author():
    from store.models import Author
    a_list=[
        {
            'name':'author 10',
            'age':25
        },
        {
            'name':'author 11',
            'age':26
        },
        {
            'name':'author 12',
            'age':25
        }
        ]
    
    for a in a_list:
        Author.objects.create(
            name=a['name'],
            age=a['age'])
            
            
def publisher():
    from store.models import Publisher
    p_list=[
        {
            'name':'publisher 10',
            
        },
        {
            'name':'publisher 11',
            
        },
        {
            'name':'publisher 12',
            
        },
        ]
    
    for p in p_list:
        Publisher.objects.create(
            name=p['name']
            )


def book():
    from store.models import Publisher,Author,Book
    b_list=[
        {
            'name':'book 12',
            'price':100,
            'rating':5.6,
            'pubdate':'2000-10-10',
            'authors':[
                {
                    'name':'author 1'
                },
                {
                    'name':'author 2'
                }
                ],
            'publisher':'publisher 12'
                
            
        },
        {
            'name':'book 11',
            'price':150,
            'rating':7.0,
            'pubdate':'2000-10-10',
            'authors':[
                {
                    'name':'author 1'
                },
                
                {
                    'name':'author 11'
                }
                ],
            'publisher':'publisher 11'
                
            
        }
        ]
    
    for b in b_list:
        p=Publisher.objects.filter(name=b['publisher'])[0]
        k=Book.objects.create(
            name=b['name'],
            rating=b['rating'],
            pubdate=b['pubdate'],
            price=b['price'],
            publisher=p
            )
        for a in b['authors']:
            a=Author.objects.filter(name=a['name'])[0]
            k.authors.add(a)
            k.save()


def store():
    from store.models import Store,Book
    s_list=[
        {
            'name':'store 12',
            'books':[
                {
                    'name':'book 1'
                },
                {
                    'name':'book 12'
                },
                {
                    'name':'book 10'
                },
                
                ]
        },
        {
            'name':'store 13',
            'books':[
                {
                    'name':'book 12'
                },
                {
                    'name':'book 11'
                },
                {
                    'name':'book 1'
                }
                ]
        }
        ]
    
    for s in s_list:
        
        k=Store.objects.create(
            name=s['name'])
            
        for a in s['books']:
            a=Book.objects.filter(name=a['name'])[0]
            k.books.add(a)
            k.save()
