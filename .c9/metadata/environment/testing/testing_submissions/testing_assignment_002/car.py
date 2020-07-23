{"filter":false,"title":"car.py","tooltip":"/testing/testing_submissions/testing_assignment_002/car.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":62,"column":12},"action":"insert","lines":["class Car:","    def __init__(self,max_speed,acceleration,tyre_friction,color='Blue'):","        ","        if max_speed<=0:","            raise ValueError('Invalid value for max_speed')","        if acceleration<=0:","            raise ValueError('Invalid value for acceleration')","        if tyre_friction<=0:","            raise ValueError('Invalid value for tyre_friction')","        ","        self._max_speed=max_speed","        self._tyre_friction=tyre_friction","        self._acceleration=acceleration","        self._color=color","        self._horn=\"Beep Beep\"","        self._is_engine_started=False","        self._current_speed=0","     ","    @property","    def max_speed(self):","        return self._max_speed","    @property","    def tyre_friction(self):","        return self._tyre_friction","           ","    @property","    def acceleration(self):","        return self._acceleration","    @property","    def color(self):","        return self._color","    @property","    def is_engine_started(self):","        return self._is_engine_started","    @property","    def current_speed(self):","        return self._current_speed","   ","    def start_engine(self):","        self._is_engine_started=True","        ","    def stop_engine(self):","        self._is_engine_started=False","        ","    def accelerate(self):","        if self._is_engine_started:","            self._current_speed+=self._acceleration","            if(self._current_speed>self._max_speed):","                self._current_speed=self._max_speed","        else:","            print('Start the engine to accelerate')","            ","    def apply_brakes(self):","            self._current_speed-=self._tyre_friction","            if(self._current_speed<=0):","                self._current_speed=0","                ","    def sound_horn(self):","        if self._is_engine_started:","            print(self._horn)","        else:","            print('Start the engine to sound_horn')","            "],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":62,"column":12},"end":{"row":62,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1586932714377,"hash":"5ecf9d86ae4a18dfbb788a0d65edf7a8bf831b8b"}