
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
        
        
    
class Store:
    list_of_items=[]
    def __init__(self,list=None):
        
    def add_item(self,list=None):
        type(self).l


store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  


>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> print(store)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food