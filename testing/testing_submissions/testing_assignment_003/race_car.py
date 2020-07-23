from car import Car
import math

class RaceCar(Car):
    def __init__(self,max_speed,acceleration,tyre_friction,color='Blue'):
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
                if(self._nitro<=0):
                    self._nitro=0
            if(self._current_speed>self._max_speed):
                self._current_speed=self._max_speed
        else:
            print('Start the engine to accelerate')
        
            
    def apply_brakes(self):
        if (self._current_speed>(self._max_speed)/2) and self.is_engine_started:
            self._nitro+=10
        super().apply_brakes()
