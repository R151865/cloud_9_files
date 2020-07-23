

class Car:
    
    horn="Beep Beepk"
        
    def __init__(self,max_speed=None,acceleration=None,tyre_friction=None,color=None):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.current_speed=0
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
            if(self.current_speed<=self.max_speed):
                self.current_speed+=self.acceleration
            if(self.current_speed>=self.max_speed):
                self.current_speed=self.max_speed
        else:
            print('Start the engine to accelerate')
            
    def apply_brakes(self):
        if(self.is_engine_started):
            self.current_speed-=self.tyre_friction
            if(self.current_speed<0):
                self.current_speed=0
   
    
    def sound_horn(self):
        if(self.is_engine_started):
            print(type(self).horn)
        else:
           print('Start the engine to sound_horn')
           
    
            