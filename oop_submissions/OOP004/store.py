
class Item:
    def __init__(self,name,category,price=None):
        self.name=name
        self.category=category
        
        if(price<=0):
            self.price=0
            raise ValueError('Invalid value for price, got {}'.format(price))
        else:
            self.price=price
    def __str__(self):
        return '{}@{}-{}'.format(self.name,self.price,self.category)
        

class Query:
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
        
    def filter(self,query):
        self.list1=[]
        
        if(query.operation=='IN'):
            for items in query.value:
                for i in self.list_of_items:
                    if(i.category==items):
                        self.list1.append(i)
            
        elif(query.operation=='EQ'):
            for i in self.list_of_items:
                if( query.value==i.category or 
                query.value==i.price or query.value==i.name):
                    self.list1.append(i)
            
        elif(query.operation=='GT' ):
            for i in self.list_of_items:
                if(i.price>query.value):
                   self.list1.append(i)
            
        elif(query.operation=='GTE'):
            for i in self.list_of_items:
                if(i.price>=query.value):
                   self.list1.append(i)
            
        elif(query.operation=='LT'):
            for i in self.list_of_items:
                if(i.price<query.value):
                   self.list1.append(i)
            
        elif(query.operation=='LTE'):
            for i in self.list_of_items:
                if(i.price<=query.value):
                   self.list1.append(i)
            
        elif(query.operation=='STARTS_WITH'):
            for i in self.list_of_items:
                if(i.name.startswith(query.value)):
                    self.list1.append(i)
            
        elif(query.operation=='ENDS_WITH'):
            for i in self.list_of_items:
                if(i.name.endswith(query.value)):
                    self.list1.append(i)
            
        elif(query.operation=='CONTAINS'):
            for i in self.list_of_items:
                if(query.value  in i.name):
                    self.list1.append(i)
                   
        return Store(self.list1)
            
    def exclude(self,query):
        self.list1=[]
        m=[]
        x=self.filter(query)
        
        for i in self.list_of_items:
            if(i not in x.list_of_items):
                m.append(i)
        return Store(m)
        
        
        

"""
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="ParleG Biscuits", price=10, category="Food")  
store.add_item(item)  
query = Query(field="price", operation="GT", value=15)  
results = store.filter(query)  
print(results)
print()
print(store)

Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  

new_query =  Query(field="name", operation="CONTAINS", value='Boost')  
updated_results = results.exclude(new_query)  
#print()
print(updated_results)  


Oreo Biscuits@30-Food  
"""