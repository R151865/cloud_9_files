
class Animal:
    _breathe_type='Breathe in air'
    _sound_type='Buck Buck'
    
    def __init__(self,age_in_months, breed, required_food_in_kgs,age_increase=1,food_increase=2):
        if age_in_months!=1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(age_in_months))
        if required_food_in_kgs<=0:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(required_food_in_kgs))
    
        self._age_in_months=age_in_months
        self._breed =breed
        self._required_food_in_kgs=required_food_in_kgs
        self._age_increase=age_increase
        self._food_increase=food_increase
        
    @classmethod    
    def make_sound(cls):
        print(cls._sound_type)
    @classmethod
    def breathe(cls):
        print(cls._breathe_type)
    
    def grow(self):
        self._age_in_months+=self._age_increase
        self._required_food_in_kgs+=self._food_increase
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs


class Carnivores:
    def hunt(self,zoo):
        for animal in zoo._list_of_animals:
            if 'Buck Buck'==animal._sound_type:
                zoo._list_of_animals.remove(animal)
                zoo._count=len(zoo._list_of_animals)
                Zoo._all_animals_in_all_zoos-=1
                break
        else:
            print('No deers to hunt')


class Water_animal(Animal):
    _breathe_type='Breathe oxygen from water'
    

class Water_Hunters:
    def hunt(self,zoo):
        for animal in zoo._list_of_animals:
            if 'Hum Hum'==animal._sound_type:
                zoo._list_of_animals.remove(animal)
                zoo._count=len(zoo._list_of_animals)
                Zoo._all_animals_in_all_zoos-=1
                break
        else:
            print('No GoldFish to hunt')



class Deer(Animal):
    _sound_type='Buck Buck'
    
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs,age_increase=1,food_increase=2)
        
class Lion(Animal,Carnivores):
    _sound_type='Roar Roar'
        
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs,age_increase=1,food_increase=4)

class Snake(Animal,Carnivores):
    _sound_type='Hiss Hiss'
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs,age_increase=1,food_increase=0.5)
        

class Shark(Water_animal,Water_Hunters):
    _sound_type='Shark Sound'
        
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs,age_increase=1,food_increase=8)
        
        
class GoldFish(Water_animal):
    _sound_type='Hum Hum'
        
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs,age_increase=1,food_increase=0.2)
        
    
class Zoo:
    _all_animals_in_all_zoos=0
    def __init__(self):
        self._reserved_food_in_kgs=0
        self._count=0
        self._list_of_animals=[]
        
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    
    def count_animals(self):
        return self._count
        
    def add_food_to_reserve(self,food_value):
        self._reserved_food_in_kgs+=food_value
        
    def add_animal(self,animal):
        Zoo._all_animals_in_all_zoos+=1
        self._list_of_animals.append(animal)
        self._count=len(self._list_of_animals)
    
    def feed(self,animal):
        if self.reserved_food_in_kgs>0:
            self._reserved_food_in_kgs-=animal._required_food_in_kgs
            if(self._reserved_food_in_kgs<=0):
                self._reserved_food_in_kgs=0
            animal.grow()
        
    
    @staticmethod
    def count_animals_in_given_zoos(zoos_list=[]):
        c=0
        for item in zoos_list:
            c+=item._count
        return c
            
    @classmethod
    def count_animals_in_all_zoos(cls):
        return Zoo._all_animals_in_all_zoos
 
 