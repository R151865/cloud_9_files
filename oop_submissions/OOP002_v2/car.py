import math
class Car:
    def __init__(self,max_speed,acceleration,tyre_friction,color='Red'):
        
        if max_speed<=0:
            raise ValueError('Invalid value for max_speed')
        if acceleration<=0:
            raise ValueError('Invalid value for acceleration')
           
        if tyre_friction<=0:
            raise ValueError('Invalid value for tyre_friction')
        
        self._max_speed=max_speed
        self._tyre_friction=tyre_friction
        self._acceleration=acceleration
        self._color=color
        self._horn="Beep Beep"
        self._is_engine_started=False
        self._current_speed=0
     
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def color(self):
        return self._color
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def current_speed(self):
        return self._current_speed
   
    def start_engine(self):
        self._is_engine_started=True
        
    def stop_engine(self):
        self._is_engine_started=False
        
    def accelerate(self):
        if self._is_engine_started:
            self._current_speed+=self._acceleration
            if(self._current_speed>self._max_speed):
                self._current_speed=self._max_speed
        else:
            print('Start the engine to accelerate')
            
    def apply_brakes(self):
        if self._is_engine_started:
            self._current_speed-=self._tyre_friction
            if(self._current_speed<0):
                self._current_speed=0
                
    def sound_horn(self):
        if self._is_engine_started:
            print(self._horn)
        else:
            print('Start the engine to sound_horn')
            
            
class Truck(Car):
    def __init__(self,max_speed,acceleration,tyre_friction,max_cargo_weight,color='Red'):
        if max_cargo_weight<=0:
            raise ValueError('Invalid value for max_cargo_weight')
            
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._max_cargo_weight=max_cargo_weight
        self._horn='Honk Honk'
        self._load_weight=0
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    def load(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')
        
        if self._current_speed==0:
            self._load_weight+=cargo_weight
            if self._load_weight>self._max_cargo_weight:
                self._load_weight-=cargo_weight
                print('Cannot load cargo more than max limit: {}'.format(self.max_cargo_weight))
        else:
            print('Cannot load cargo during motion')
            
    def unload(self,cargo_weight):
        if cargo_weight<=0:
            raise ValueError('Invalid value for cargo_weight')
        if self._current_speed==0:
            self._load_weight-=cargo_weight
            if self._load_weight<0:
                self._load_weight=0
        else:
            print('Cannot unload cargo during motion')
        
    
class RaceCar(Car):
    def __init__(self,max_speed,acceleration,tyre_friction,color='Red'):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._nitro=0
        self._horn='Peep Peep\nBeep Beep'
        
    @property
    def nitro(self):
        return self._nitro
    
    def accelerate(self):
        if self._is_engine_started:
            self._current_speed+=self._acceleration
             #super().accelerate()
            if (self._nitro>0):
                self._current_speed+=math.ceil(self._acceleration*0.3)
                self._nitro-=10
                if(self._nitro<0):
                    self._nitro=0
            if(self._current_speed>self._max_speed):
                self._current_speed=self._max_speed
        else:
            print('Start the engine to accelerate')
        
            
    def apply_brakes(self):
        if (self._current_speed>(self._max_speed)/2) and self.is_engine_started:
            self._nitro+=10
        super().apply_brakes()
        
        

