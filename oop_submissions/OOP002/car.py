class Car:
    
    horn="Beep Beepk"
        
    def __init__(self,max_speed=None,acceleration=None,tyre_friction=None,color=None):
        self.color=color
        self.max_speed=max_speed
        self._acceleration=acceleration
        self.tyre_friction=tyre_friction
        self._current_speed=0
        self.is_engine_started=False
        
        
        if(max_speed<0):
            raise ValueError('Invalid value for max_speed')
        if( acceleration<0):
            raise ValueError('Invalid value for acceleration')
        if(tyre_friction<0):
            raise ValueError('Invalid value for tyre_friction')
        
        
    def start_engine(self):
        self.is_engine_started=True
        
    def stop_engine(self):
        self.is_engine_started=False
                
    
    def accelerate(self):
        if(self.is_engine_started):
            if(self._current_speed<=self.max_speed):
                self._current_speed+=self._acceleration
            if(self._current_speed>=self.max_speed):
                self._current_speed=self.max_speed
        else:
            print('Start the engine to accelerate')
            
    def apply_brakes(self):
        if(self.is_engine_started):
            self._current_speed-=self.tyre_friction
            if(self._current_speed<0):
                self._current_speed=0
   
    
    def sound_horn(self):
        if(self.is_engine_started):
            print(type(self).horn)
        else:
           print('Start the engine to sound_horn')
           
    
            


class Truck(Car):
    horn="Honk Honk"
    def __init__(self,max_speed,acceleration,tyre_friction,max_cargo_weight,color=None):
        self.max_cargo_weight=max_cargo_weight
        self.truck_load=0
        
        super().__init__(max_speed,acceleration,tyre_friction,color)
        
    
            
    def load(self,cargo_weight):
        if(cargo_weight>=0):
            if(self._current_speed==0):
                self.truck_load+=cargo_weight
                if(self.truck_load>self.max_cargo_weight):
                    print(f'Cannot load cargo more than max limit: {self.max_cargo_weight}')
            else:
                print("Can't load during motion")
                
        else:
            raise ValueError('Invalid for cargo_weight')
    def unload(self,cargo_weight):
        if(cargo_weight>=0):
            if(self._current_speed==0):
                self.truck_load-=cargo_weight
                if(self.truck_load<=0):
                    self.truck_load=0
            else:
                print("Can't load during motion")
                
        else:
            raise ValueError('Invalid for cargo_weight')
            
    



        
            
class RaceCar(Car):
    horn="Peep Peep\nBeep Beep"
        
    
    def __init__(self,max_speed,acceleration,tyre_friction,color=None):
        self.nitro=0
        
        super().__init__(max_speed,acceleration,tyre_friction,color)

            
    def apply_brakes(self):
        if(self.is_engine_started):
            if(self._current_speed>self.max_speed/2):
                self._current_speed-=self.tyre_friction
                self.nitro+=10
            else:
                self._current_speed-=self.tyre_friction
                 
            
    def accelerate(self):
        if(self.is_engine_started):
            if(self.nitro>0):
                self._current_speed+=self._acceleration+int(self._acceleration*0.3)
                self.nitro-=10
            else:
                self._current_speed+=self._acceleration
            
            if(self.nitro<=0):
                self.nitro=0
            if(self._current_speed>=self.max_speed):
                self._current_speed=self.max_speed
        else:
            print('Start the engine to accelerate')

