
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
        
    
class Store(Query):
    counter=0
    list_of_items=[]
    def __init__(self):
        
        self.list1=[]
        
        
    def add_item(self,list=None):
        type(self).counter+=1
        
        type(self).list_of_items.append(list)
        
        
    def count(self):            #counting 
       return type(self).counter
    
    def __str__(self):
        for i in type(self).list_of_items:
            print(i)
        return ''
    
        
    def filter(self,query):
        self.list1=[]
        x=Store()
        
        if(query.operation=='IN'):
            for items in query.value:
                for i in type(self).list_of_items:
                    if(i.category==items):
                        print(i)
                
        elif(query.operation=='EQ'):
            for i in type(self).list_of_items:
                if query.value==i.category or query.value==i.price or query.value==i.name :
                    print(i)
                
        elif(query.operation=='GT' ):
            for i in type(self).list_of_items:
                print(i.price)
                if(i.price>query.value):
                    print(i)
                    
        elif(query.operation=='GTE'):
            for i in type(self).list_of_items:
                if(i.price>=query.value):
                    print(i)
            
        elif(query.operation=='LT'):
            for i in type(self).list_of_items:
                if(i.price<query.value):
                    print(i)
        elif(query.operation=='LTE'):
            for i in type(self).list_of_items:
                if(i.price<=query.value):
                    print(i)
        elif(query.operation=='STARTS_WITH'):
            for i in type(self).list_of_items:
                if(i.name.startswith(query.value)):
                    print(i)
        elif(query.operation=='ENDS_WITH'):
            for i in type(self).list_of_items:
                if(i.name.endswith(query.value)):
                    print(i)
        elif(query.operation=='CONTAINS'):
            for i in type(self).list_of_items:
                if(query.value  in i.name):
                    self.list1.append(i)
                    x.add_item(i)
            return x       
            
                   
                   
            
              
            
    def exclude(self,query):
        
        if(query.operation=='IN'):
            for items in query.value:
                for i in type(self).list_of_items:
                    if(i.category!=items):
                        print(i)
                
        elif(query.operation=='EQ'):
            for i in type(self).list_of_items:
                if query.value!=i.category or query.value!=i.price or query.value!=i.name :
                    print(i)
                
        elif(query.operation=='GT' ):
            for i in type(self).list_of_items:
                
                if(i.price<query.value):
                    print(i)
                    
        elif(query.operation=='GTE'):
            for i in type(self).list_of_items:
                if(i.price<=query.value):
                    print(i)
            
        elif(query.operation=='LT'):
            for i in type(self).list_of_items:
                if(i.price>query.value):
                    print(i)
        elif(query.operation=='LTE'):
            for i in type(self).list_of_items:
                if(i.price>=query.value):
                    print(i)
        elif(query.operation=='STARTS_WITH'):
            for i in type(self).list_of_items:
                if(not(i.name.startswith(query.value))):
                    print(i)
        elif(query.operation=='ENDS_WITH'):
            for i in type(self).list_of_items:
                if(not(i.name.endswith(query.value))):
                    print(i)
        elif(query.operation=='CONTAINS'):
            for i in type(self).list_of_items:
                if(not(query.value  in i.name)):
                    print(i)
            

store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item)  
query = Query(field="name", operation="CONTAINS", value="uit")  
results = store.filter(query) 

print(results)  

"""
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food   

Butter@10-Grocery            
            

print(results)

Oreo Biscuits@30-Food  
Boost Biscuits@20-Food              
   """    