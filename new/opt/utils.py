from opt.models import *
from collections import defaultdict
from django.db.models import Sum,Avg,Max,Min,Count,Q

def profile():
    def decorator(func):
        def handler(*args, **kwargs):
            import line_profiler
            profiler = line_profiler.LineProfiler()
            profiler.enable_by_count()
            profiler.add_function(func)
            result = func(*args, **kwargs)
            profiler.print_stats()
            return result

        handler.__doc__ = func.__doc__
        return handler

    return decorator
    


@profile()
def my_function():
    import time
    time.sleep(2)
    print('Exiting my function')




@profile()
def get_books_by_author_select_related():
    from opt.models import Book
    from collections import defaultdict
    books=Book.objects.all().select_related('author')
    
    result = defaultdict(list)
    for book in books:
        author = book.author
        title_and_author = '{} by {}'.format(
            book.title,
            author.name
        )
        result[book.library_id].append(title_and_author)
    return result

@profile()
def get_books_by_author_select_related_values():
    books=Book.objects.all().values(
        'title','library_id','author__name')
    
    result = defaultdict(list)
    for book in books:
        title_and_author = '{} by {}'.format(
            book['title'],
            book['author__name']
        )
        result[book['library_id']].append(title_and_author)
    return result

@profile()
def get_books_by_author_select_related_values_list():
    books=Book.objects.all().values_list(
        'title','library_id','author__name')
    
    result = defaultdict(list)
    for book in books:
        title_and_author = '{} by {}'.format(
            book[0],
            book[2]
        )
        result[book[1]].append(title_and_author)
    return result


@profile()
def get_page_count_by_library_id():
    result=defaultdict(int)
    books=Book.objects.all().prefetch_related('pages')
    for book in books:
        result[book.library_id]+=book.get_page_count()
    return result
    
@profile()
def get_page_count_by_library_id_using_annotation():
    result={}
    libraries=(
        Library.objects
        .all()
        .annotate(page_count=Sum('books__pages'))
        .values_list('id','page_count')
        
        )
    for library_id,page_count in libraries:
        result[library_id]=page_count
    return result

@profile()
def t1():
    count = Book.objects.filter(author_id=1).count()
    Book.objects.filter(id=3).exists()  

@profile()
def t2():  
    count = len(Book.objects.filter(author_id=1))
    Book.objects.get(id=3)







































def pop_lib():
    lib_list=[
        {
            'name':'library 1',
            'address':'address 1'
        },
        {
            'name':'library 2',
            'address':'address 2'
        },
        {
            'name':'library 3',
            'address':'address 3'
        },
        {
            'name':'library 4',
            'address':'address 4'
        },        
        ]
    for item in lib_list:
        Library.objects.create(
            name=item['name'],
            address=item['address']
            )
        
def pop_author():
    auth_list=[
        {
            'name':'author 1'
        },
        {
            'name':'author 2'
        }, 
        {
            'name':'author 3'
        },
        {
            'name':'author 4'
        }
        ]
    for item in auth_list:
        Author.objects.create(
            name=item['name']
            )
def pop_book():
    """
    {
            'title':'book 1',
            'address':'book 1 address',
            'author':'author 1',
            'library':'library 1'
        }
    """
    book_list=[
        {
            'title':'book 2',
            'address':'book 2 address',
            'author':'author 2',
            'library':'library 2'
        },
        {
            'title':'book 3',
            'address':'book 3 address',
            'author':'author 3',
            'library':'library 3'
        },
        {
            'title':'book 4',
            'address':'book 4 address',
            'author':'author 2',
            'library':'library 1'
        },
        {
            'title':'book 5',
            'address':'book 5 address',
            'author':'author 1',
            'library':'library 2'
        }

        
        ]
        
    for item in book_list:
        auth=Author.objects.filter(name=item['author'])[0]
        lib=Library.objects.filter(name=item['library'])[0]
        Book.objects.create(
            title=item['title'],
            address=item['address'],
            author=auth,
            library=lib
            )

def pop_page():
    """
    {   'book':'book 1',
            'text':'book 1 text',
            'page_number':1
        }
    """
    page_list=[
        {   'book':'book 1',
            'text':'book 1 text',
            'page_number':2
        },
        {   'book':'book 2',
            'text':'book 2 text',
            'page_number':2
        },
        
        {   'book':'book 2',
            'text':'book 2 text',
            'page_number':5
        },
        {   'book':'book 4',
            'text':'book 4 text',
            'page_number':2
        },
        {   'book':'book 3',
            'text':'book 3 text',
            'page_number':5
        },
        {   'book':'book 3',
            'text':'book 3 text',
            'page_number':7
        }
        
        
        ]
        
        
    for item in page_list:
        bok=Book.objects.filter(title='book 1')[0]
        
        Page.objects.create(
            text=item['text'],
            page_number=item['page_number'],
            book=bok
            )