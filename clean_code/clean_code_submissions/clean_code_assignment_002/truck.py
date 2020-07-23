from car import Car


class Truck(Car):
    def __init__(self, max_speed, acceleration, tyre_friction,
                 max_cargo_weight,
                 color='Blue'):
        if max_cargo_weight <= 0:
            raise ValueError('Invalid value for max_cargo_weight')
        super().__init__(max_speed, acceleration, tyre_friction, color)
        self._max_cargo_weight = max_cargo_weight
        self._horn = 'Honk Honk'
        self._load_weight = 0

    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight

    @property
    def load_weight(self):
        return self._load_weight

    def is_valid_cargo_weight(self, cargo_weight):
        if cargo_weight <= 0:
            raise ValueError('Invalid value for cargo_weight')

    def load(self, cargo_weight):
        self.is_valid_cargo_weight(cargo_weight)
        if self._current_speed == 0:
            self._load_weight += cargo_weight
            if self._load_weight > self._max_cargo_weight:
                self._load_weight -= cargo_weight
                print('Cannot load cargo more than'
                      ' max limit: {}'.format(self.max_cargo_weight))
        else:
            print('Cannot load cargo during motion')

    def unload(self, cargo_weight):
        self.is_valid_cargo_weight(cargo_weight)
        if self._current_speed == 0:
            self._load_weight -= cargo_weight
            if self._load_weight < 0:
                self._load_weight = 0
        else:
            print('Cannot unload cargo during motion')
