
class Deer:
    air_breath='Breathe in air'
    sound='Buck Buck'
    
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        
        self.age_increase=1
        self.food_increase=2
        
        if(self._age_in_months!=1):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        if(self._required_food_in_kgs<=0):
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
        
    def get_age_in_months(self):
        return self._age_in_months
    age_in_months=property(get_age_in_months)
    
    def get_breed(self):
        return self._breed
    breed=property(get_breed)
    
    def get_required_food_in_kgs(self):
        return self._required_food_in_kgs
    required_food_in_kgs=property(get_required_food_in_kgs)
        
    
        
    def grow(self):
        self._age_in_months+=self.age_increase
        self._required_food_in_kgs+=self.food_increase
        
      
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
    
    @classmethod
    def breathe(cls):
        print(cls.air_breath)


class Lion(Deer):
    sound='Roar Roar'
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.age_increase=1
        self.food_increase=4
        
    def hunt(self,zoo):
        for i in zoo.list_of_animals:
            if(i.sound==Deer.sound):
                    zoo.list_of_animals.remove(i)
                    zoo.count=len(zoo.list_of_animals)
        
                    break
        else:
            print('No deers to hunt')
            
            
    
class Shark(Deer):
    sound='Shark Sound'
    air_breath="Breathe oxygen from water"
    
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.age_increase=1
        self.food_increase=8
       
    def hunt(self,zoo):
        for i in zoo.list_of_animals:
            if(i.sound==GoldFish.sound):
                    zoo.list_of_animals.remove(i)
                    zoo.count=len(zoo.list_of_animals)
                    break
        else:
            print('No GoldFish to hunt')
    
    
    
       
class GoldFish(Shark):
    sound="Hum Hum"
    #air_breath="Breathe oxygen from water"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.age_increase=1
        self.food_increase=0.2

class Zoo:
    animals_in_all_zoos=0
    
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.count=0
        self.list_of_animals=[]
        
    
    def count_animals(self):
        return self.count
    
    #encapsulation for zoo
    def get_reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    reserved_food_in_kgs=property(get_reserved_food_in_kgs)
        
    
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
        
    def add_animal(self,animal):
        Zoo.animals_in_all_zoos+=1
        self.list_of_animals.append(animal)
        self.count=len(self.list_of_animals)
        
    def feed(self,animal):
        self._reserved_food_in_kgs-=animal._required_food_in_kgs
        if(self._reserved_food_in_kgs<0):
            self._reserved_food_in_kgs=0
        
    @staticmethod    
    def count_animals_in_all_zoos():
        return Zoo.animals_in_all_zoos
    
    @staticmethod    
    def count_animals_in_given_zoos(list):
        c=0
        for i in list:
            c+=i.count
        return c


class Snake(Lion):
    sound="Hiss Hiss"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.age_increase=1
        self.food_increase=0.5
        
    
        
"""
#from zoo import Snake
snake = Snake(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=5)
print(snake.age_in_months)
#1
print(snake.breed)
"Indian Cobra"
print(snake.required_food_in_kgs)
#5
snake.grow()
print(snake.required_food_in_kgs)
#5.5
print(snake.age_in_months)
#2
snake.make_sound() # Prints
"Hiss Hiss"
snake.breathe() # Prints
"Breathe in air"
"""
"""

zoo = Zoo()
zoo.add_food_to_reserve(100)
deer = Deer(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=50)
lion = Lion(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=50)
snake = Snake(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=50)
zoo.add_animal(deer)
zoo.add_animal(deer)
zoo.add_animal(deer)
#zoo.add_animal(deer)
snake.hunt(zoo)
print(zoo.count)

#lion.hunt(zoo)
#lion.hunt(zoo)
"""


"""
snake = GoldFish(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=5000000)
snake.grow()
print(zoo.reserved_food_in_kgs)

zoo.feed(snake)

print(zoo.reserved_food_in_kgs)
#print(snake.required_food_in_kgs)
"""



"""

zoo=Zoo()
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
zoo.add_animal(deer)
zoo.add_animal(deer)
zoo.add_animal(deer)
snake=Snake(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
snake.hunt(zoo)
#snake.hunt(zoo)

snake.hunt(zoo)

#print(zoo.count_animals())
"""
"""
l=Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
zoo=Zoo()
zoo.add_food_to_reserve(1000)
print(zoo.reserved_food_in_kgs)
"""


"""
l=Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
zoo.add_animal(l)
nehru_zoological_park = Zoo()
zoo.add_food_to_reserve(10000000)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(nehru_zoological_park.count_animals())
#1
print(Zoo.count_animals_in_all_zoos())
#2
print(Zoo.count_animals_in_given_zoos([zoo,nehru_zoological_park]))
#1
# from zoo import Deer
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
nehru_zoological_park.count_animals()
#2
lion.hunt(nehru_zoological_park)
nehru_zoological_park.count_animals()
#1
print(lion.hunt(nehru_zoological_park))
#No deers to hunt
#
"""