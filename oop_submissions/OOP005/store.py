# have to recheck the  equal 
class Item:
    def __init__(self,name,category,price=0):
        self.name=name
        self.category=category
        self.price=price
        
        if(price<=0):
            raise ValueError('Invalid value for price, got {}'.format(price))
        
    def __str__(self):
        return '{}@{}-{}'.format(self.name,self.price,self.category)
        

class Query(Item):
    def __init__(self,field,operation,value):
        self.field=field
        self.operation=operation
        self.value=value
        
        if(self.operation!='IN' and self.operation!='EQ'and 
        self.operation!='GT' and self.operation!='GTE' and 
        self.operation!='LT' and self.operation!='LTE' and 
        self.operation!='STARTS_WITH' and self.operation!='ENDS_WITH'and
        self.operation!='CONTAINS'):
            raise ValueError('Invalid value for operation, got {}'.format(self.operation))
        
    def __str__(self):
        return '{} {} {}'.format(self.field,self.operation,self.value)
        
    
class Store(Query,Item):
    
    def __init__(self,l=[]):
        self.counter=0
        self.list_of_items=l
        self.list1=[]
        
    def add_item(self,list=None):
       if(list!=None):
            self.counter+=1
            self.list_of_items.append(list)
        
    def count(self):            #counting 
       return self.counter
    
    def __str__(self):
        if(len(self.list_of_items)):
            w=[str(u) for u in self.list_of_items]
            return '\n'.join(w)
        else:
            return 'No items'
        
    
    def __add__(self,a):
        empt=[]
        self.list1=[]
        for i in a.list_of_items:
            empt.append(i)
        for j in self.list_of_items:
            empt.append(j)
        self.list1=empt
        return Store(self.list1)
    
    
        
    def filter(self,*arg):
        sb=self.list_of_items
        for query in arg:
            self.list1=[]
            if(query.operation=='IN'):
                for items in query.value:
                    for i in sb:
                        if(i.category==items):
                            self.list1.append(i)
                
            elif(query.operation=='EQ'):
                for i in sb:
                    if query.value==i.category or query.value==i.price or query.value==i.name :
                        self.list1.append(i)
                
            elif(query.operation=='GT' ):
                for i in sb:
                    if(i.price>query.value):
                       self.list1.append(i)
                
            elif(query.operation=='GTE'):
                for i in sb:
                    if(i.price>=query.value):
                       self.list1.append(i)
                
            elif(query.operation=='LT'):
                for i in sb:
                    if(i.price<query.value):
                       self.list1.append(i)
                
            elif(query.operation=='LTE'):
                for i in sb:
                    if(i.price<=query.value):
                       self.list1.append(i)
                
            elif(query.operation=='STARTS_WITH'):
                for i in sb:
                    if(i.name.startswith(query.value)):
                        self.list1.append(i)
                
            elif(query.operation=='ENDS_WITH'):
                for i in sb:
                    if(i.name.endswith(query.value)):
                        self.list1.append(i)
                
            elif(query.operation=='CONTAINS'):
                for i in sb:
                    if(query.value  in i.name):
                        self.list1.append(i)
                        
            sb=self.list1
                       
        return Store(sb)

      
    
    #i did not understand what is going on here
    def exclude(self,*arg):
        sb=self.list_of_items
        for query in arg:
            self.list1=[]
            m=[]
            x=self.filter(query)
            for i in sb:
                if(i not in x.list_of_items):
                    m.append(i)        
            sb=m
        return Store(sb)
            
       
        
"""
store = Store()
item = Item(name="Oreo Biscuits", price=30, category="Food")
store.add_item(item)
item = Item(name="Boost Biscuits", price=20, category="Food")
store.add_item(item)
item = Item(name="ParleG Biscuits", price=10, category="Food")
store.add_item(item)
print(store)
print()


Oreo Biscuits@30-Food
Boost Biscuits@20-Food
ParleG Biscuits@10-Food

k = Query(field="price", operation="GT", value=15)
query = Query(field="name", operation="CONTAINS", value="oo")

results = store.filter(k, query) # should be able to give any number of Query objects as arguments
print(results)
print()

Boost Biscuits@20-Food


results = store.exclude(query,k) # should be able to give any number of Query objects as arguments
print(results)

Oreo Biscuits@30-Food
ParleG Biscuits@10-Food
"""