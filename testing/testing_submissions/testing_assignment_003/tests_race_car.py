import pytest

@pytest.fixture
def race_car1():
    from race_car import RaceCar
    max_speed =50
    acceleration = 10
    tyre_friction = 5
    race_car_obj=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    return race_car_obj
    
@pytest.fixture
def race_car():
    from race_car import RaceCar
    color='Blue'
    max_speed=40
    acceleration=10
    tyre_friction=3
    race_car_obj=RaceCar(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    return race_car_obj


# test to half_of_max_speed
def test_apply_brakes_when_current_speed_is_equal_to_half_of_max_speed_should_return_nitro_zero():
    # Arrange
    from race_car import RaceCar
    max_speed=7
    acceleration= 3.5
    tyre_friction=1
    nitro_value=0
    
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    
    # Act
    race_car.apply_brakes()
    
    # Assert
    assert race_car.nitro == nitro_value


# test case to check wether nitro is zero or not when nitro become negative

def test_nitro_edge_condition_when_nitro_becomes_negative_but_should_return_zero():
    # Arrange
    from race_car import RaceCar
    max_speed =20
    acceleration = 11
    tyre_friction = 9
    nitro_value_should_be_zero = 0
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    
    # Act
    race_car.apply_brakes()
    race_car.accelerate()
    
    
    # Assert
    assert race_car.nitro == nitro_value_should_be_zero 




@pytest.mark.parametrize('max_speed,acceleration,tyre_friction',[
    (10,10,10),(1,1,1),(1,10,1)
    ])
def test_nitro_when_created_race_car_should_return_nitro_value_zero(max_speed,acceleration,tyre_friction):
    # Arrange
    from race_car import RaceCar
    nitro_value_should_be_zero=0
    
    # Act
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert race_car.nitro == nitro_value_should_be_zero
    

@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,nitro_value',[
    (10,10,5,10),(10,1,9,0),(5,3,1,10),(5,10,1,20),(10,1,1,0),(6,5,2,10)
    ])
def test_nitro_on_applying_brakes_when_current_speed_less_than_equal_to_and_greater_than_half_of_max_speed(nitro_value,max_speed,acceleration,tyre_friction):
    # Arrage
    from race_car import RaceCar
    is_engine_started_is_true= True
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    
    # Act
    race_car.apply_brakes()
    race_car.apply_brakes()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_true
    assert race_car.nitro == nitro_value
    
#test_nitro_whether_nitro_adding_or_not_to_acceleration_when_available

@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,current_speed,nitro_value',[
    (10,10,5,10,0),(20,10,10,10,0),(20,11,10,16,0)
    ])
def test_nitro_whether_nitro_adding_or_not_to_acceleration_when_available(nitro_value,current_speed,max_speed,acceleration,tyre_friction):
    # Arrage
    from race_car import RaceCar
    is_engine_started_is_true= True
    nitro_value=nitro_value
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.apply_brakes() 
    
    # Act
    race_car.accelerate()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_true
    assert race_car.nitro == nitro_value
    assert race_car.current_speed == current_speed


@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,nitro_value',[
    (50,30,1,20),(20,11,1,0),(20,12,1,10),(20,13,1,20)
    ])
def test_nitro_whether_is_it_reducing_or_not_when_accelerate(max_speed,acceleration,tyre_friction,nitro_value):
    # Arrage
    from race_car import RaceCar
    is_engine_started_is_true= True
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    
    # Act
    race_car.accelerate()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_true
    assert race_car.nitro == nitro_value
    
def test_nitro_whether_is_it_displaying_nitro_value(race_car1):
    # Arrage
    nitro_value = 20 
    race_car = race_car1
    is_engine_started_is_true =True
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    
    # Act
    race_car.apply_brakes()
    race_car.apply_brakes()
    
    # Assert 
    assert race_car.is_engine_started == is_engine_started_is_true
    assert type(race_car.nitro) == int
    assert race_car.nitro == nitro_value
    

def test_encapsulation_of_nitro_when_try_to_assign_raise_attribute_error(race_car1):
    # Arrange
    race_car=race_car1
    value_error_message_to_is_nitro="can't set attribute"
    value_assigning_to_private_variable= 1
    
    # Act
    with pytest.raises(Exception) as error:
        race_car.nitro = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) == value_error_message_to_is_nitro

@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,current_speed',[
    (20,4,1,18),(30,7,3,23)
    ])

def test_acceleration_with_multiple_acceleration_and_brakes_by_checking_current_speed(current_speed,max_speed,acceleration,tyre_friction):
    # Arrange
    from race_car import RaceCar
    is_engine_started_is_true= True
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    
    
    #Act
    race_car.accelerate()
    race_car.accelerate()
   
    # Assert 
    assert race_car.current_speed == current_speed
        




# Task-1 Creating race_car
def test_creating_multiple_race_car_instances_with_valid_details():
    # Arrange
    from race_car import RaceCar
    max_speed_1=30
    acceleration_1=12
    tyre_friction_1=11
    color_1='Blue'

    max_speed_2=330
    acceleration_2=50
    tyre_friction_2=30
    color_2='White'
    
    # Act
    race_race_car_1=RaceCar(color=color_1,max_speed=max_speed_1,acceleration=acceleration_1,tyre_friction=tyre_friction_1)
    race_race_car_2=RaceCar(color=color_2,max_speed=max_speed_2,acceleration=acceleration_2,tyre_friction=tyre_friction_2)
    
    # Assert
    assert race_race_car_1.color == color_1
    assert race_race_car_1.max_speed ==max_speed_1
    assert race_race_car_1.tyre_friction ==tyre_friction_1
    assert race_race_car_1.acceleration ==acceleration_1
    
    assert race_race_car_2.color == color_2
    assert race_race_car_2.max_speed ==max_speed_2
    assert race_race_car_2.tyre_friction ==tyre_friction_2
    assert race_race_car_2.acceleration ==acceleration_2
 
def test_create_race_car_when_color_not_given_return_default_color_blue():
    # Arrange
    from race_car import RaceCar
    max_speed=40
    acceleration=10
    tyre_friction=3
    default_race_car_color_is_blue='Blue'
    
    # Act
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert race_car.color == default_race_car_color_is_blue
    


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(-1,10,3),(0,3,10)])
def test_init_function_when_max_speed_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from race_car import RaceCar
    Invalid_value_for_max_speed='Invalid value for max_speed'
    
    # Act
    with pytest.raises(ValueError) as error:
        race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert  str(error.value) == Invalid_value_for_max_speed


def test_init_function_when_valid_max_speed_is_given_do_not_raise_error():
    # Arrange
    from race_car import RaceCar
    max_speed=1
    acceleration=1
    tyre_friction=1
    
    
    # Act
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert race_car.max_speed == max_speed


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(30,-1,3),(40,0,10)])
def test_init_function_when_acceleration_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from race_car import RaceCar
    Invalid_value_for_acceleration='Invalid value for acceleration'
    
    # Act
    with pytest.raises(ValueError) as error:
        race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert  str(error.value) == Invalid_value_for_acceleration
    
    
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(30,10,-1),(40,10,0)])
def test_init_function_when_tyre_friction_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from race_car import RaceCar
    Invalid_value_for_tyre_friction='Invalid value for tyre_friction'
    
    # Act
    with pytest.raises(ValueError) as error:
        race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert  str(error.value) == Invalid_value_for_tyre_friction


#Task-2

def test_start_engine_is_engine_started_return_true(race_car):
    # Arrange
    race_car=race_car
    is_engine_started=True
    
    # Act
    race_car.start_engine()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started
    
    
def test_start_engine_when_intially_is_at_rest_and_current_speed_zero(race_car):
    # Arrange
    intial_current_speed_of_race_car=0
    is_engine_started=True
    
    # Act
    race_car.start_engine()
    
    # Assert
    assert race_car.is_engine_started== is_engine_started
    assert race_car.current_speed == intial_current_speed_of_race_car


# Task 3
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed", [
    (30,10,3,20),(10,5,5,10),(10,6,5,10)])
def test_start_engine_when_engine_started_and_accelerated_by_checking_current_speed(max_speed, acceleration, tyre_friction,current_speed):
    # Arrange
    from race_car import RaceCar
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    current_speed=current_speed
    is_engine_started=True
    race_car.start_engine()
    
    # Act
    race_car.accelerate()
    race_car.accelerate()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started
    assert race_car.current_speed == current_speed
    
# Task 4
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed", [
    (30,29,3,29),(30,31,1,30),(30,30,30,30)])
def test_accelerate_when_engine_started_return_current_speed(max_speed, acceleration, tyre_friction,current_speed):
    # Arrange
    from race_car import RaceCar
    race_car_current_speed_after_acceleration=current_speed
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    is_engine_started= True
    race_car.start_engine()
    
    # Act
    race_car.accelerate()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started
    assert race_car.current_speed ==  race_car_current_speed_after_acceleration
   
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [
    (30,29,3),(50,35,1),(10,5,3)
    ])
def test_accelerate_above_max_speed_and_current_speed_is_equal_to_max_speed_only(max_speed, acceleration, tyre_friction):
    # Arrange
    from race_car import RaceCar
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car_max_speed=max_speed
    is_engine_started =True
    race_car.start_engine()
    
    # Act
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started
    assert race_car.current_speed == race_car_max_speed

def test_accelerate_when_race_car_is_not_started_print_message(race_car,capsys):
    # Arrange
    race_car=race_car
    message_to_start_engine_to_accelerate='Start the engine to accelerate\n'
    is_engine_started=False
    
    # Act
    race_car.accelerate()
    output=capsys.readouterr()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started
    assert output.out == message_to_start_engine_to_accelerate



def test_stop_engine_when_current_speed_is_not_zero_and_engine_stopped_suddenly_but_current_speed_should_be_not_zero(race_car):
    # Arrage
    race_car=race_car
    race_car.start_engine()
    race_car.accelerate()
    current_speed_after_engine_stopped=10
    is_engine_started=False
    
    # Act
    race_car.stop_engine()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started
    assert race_car.current_speed == current_speed_after_engine_stopped

def test_start_engine_with_multiple_engine_starts_and_stops_but_current_speed_should_not_be_zero(race_car):
    # Arrange
    race_car=race_car
    race_car.start_engine()
    race_car.accelerate()
    race_car.stop_engine()
    current_speed_after_all=20
    
    # Act
    race_car.start_engine()
    race_car.accelerate()
    
    # Assert
    assert race_car.current_speed == current_speed_after_all
    

# Task-5
"""
@pytest.mark.parametrize("special_case_value,return_value", [
    (-1,0),(0,0),(1,1),(2,2),(-2,0)])
def test_apply_brakes_when_engine_started_with_edge_condition(special_case_value,return_value):
    # Arrange
    from race_car import RaceCar
    max_speed=40
    acceleration=10
    tyre_friction=4
    color='Blue'
    
    race_car=RaceCar(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    
    # Actp
    race_car._tyre_friction=0
    race_car._current_speed=special_case_value
    race_car.apply_brakes()
    
    # Assert
    assert race_car.current_speed == return_value
   """
  
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed", [
    (30,10,5,5),(40,2,1,1),(40,30,10,20)])
def test_apply_brakes_when_engine_started_and_accelerated_return_current_speed(max_speed,acceleration,tyre_friction,current_speed):
    # Arrage
    from race_car import RaceCar
    race_car=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    current_speed=current_speed
    is_engine_started = True
    
    # Act
    race_car.apply_brakes()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started 
    assert race_car.current_speed == current_speed
  

def test_apply_brakes_when_engine_is_at_rest_and_not_started_then_current_speed_zero(race_car):
    # Arrange
    race_car=race_car
    current_speed=0
    is_engine_started_is_false= False
    
    # Act
    race_car.apply_brakes()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_false
    assert race_car.current_speed == current_speed

def test_apply_brakes_with_multiple_times_but_current_speed_should_not_be_negative_value_but_it_should_be_zero_only(race_car):
    # Arrange
    race_car=race_car
    race_car.start_engine()
    race_car.accelerate()
    current_speed_should_be_zero=0
    
    # Act
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    
    # assert
    assert race_car.current_speed == current_speed_should_be_zero
    
def test_apply_brakes_when_current_speed_is_some_value_and_engine_is_started_accelerated_stopped_and_checking_current_speed_is_correct_or_not(race_car):
    # Arrange
    race_car=race_car
    race_car.start_engine()
    race_car.accelerate()
    race_car.stop_engine()
    current_speed=10
    is_engine_started_is_false =False
    
    # Act
    race_car.apply_brakes()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_false
    assert race_car.current_speed == current_speed 


# Task 5
def test_sound_horn_when_race_car_engine_started_and_print_beep_beep(race_car,capsys):
    # Arrange
    race_car=race_car
    race_car.start_engine()
    peep_and_beep_sound='Peep Peep\nBeep Beep\n'
    is_engine_started_is_true=True
    
    # Act
    race_car.sound_horn()
    output=capsys.readouterr()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_true
    assert output.out == peep_and_beep_sound


def test_sound_horn_when_race_car_engine_stopped_return_string(race_car,capsys):
    # Arrange
    race_car=race_car
    start_engine_to_sound_horn_string='Start the engine to sound_horn\n'
    is_engine_started_is_false=False
   
    # Act
    race_car.sound_horn()
    output=capsys.readouterr()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_false
    assert output.out == start_engine_to_sound_horn_string


# Task -7 
def test_stop_engine_is_engine_started_return_false(race_car):
    # Arrange
    race_car=race_car
    race_car.start_engine()
    is_engine_started_is_false=False
    
    # Act
    race_car.stop_engine()
    
    # Assert
    assert race_car.is_engine_started == is_engine_started_is_false
    

# Task 8
def test_encapsulation_for_current_speed_when_try_to_assign_raise_attribute_error(race_car):
    # Arrange
    race_car=race_car
    value_error_message_to_current_speed="can't set attribute"
    value_assigning_to_private_variable=0
    
    # Act
    with pytest.raises(Exception) as error:
        race_car.current_speed = value_assigning_to_private_variable
    
    # Assert
    assert  str(error.value) ==  value_error_message_to_current_speed

def test_encapsulation_for_acceleration_when_try_to_assign_raise_attribute_error(race_car):
    # Arrange
    race_car=race_car
    value_error_message_to_acceleration="can't set attribute"
    value_assigning_to_private_variable=5
    
    # Act
    with pytest.raises(Exception) as error:
        race_car.acceleration = value_assigning_to_private_variable
    
    # Assert
    assert  str(error.value) == value_error_message_to_acceleration
    
    
def test_encapsulation_for_color_when_try_to_assign_raise_attribute_error(race_car):
    # Arrange
    race_car=race_car
    value_error_message_to_color="can't set attribute"
    value_assigning_to_private_variable='Black'
    
    # Act
    with pytest.raises(Exception) as error:
        race_car.color = value_assigning_to_private_variable
    
    # Assert
    assert  str(error.value) ==  value_error_message_to_color
    
def test_encapsulation_for_tyre_friction_when_try_to_assign_raise_attribute_error(race_car):
    # Arrange
    race_car=race_car
    value_error_message_to_tyre_friction="can't set attribute"
    value_assigning_to_private_variable =5
    
    # Act   
    with pytest.raises(Exception) as error:
        race_car.tyre_friction = value_assigning_to_private_variable
    
    # Assert
    assert  str(error.value) ==  value_error_message_to_tyre_friction
    
def test_encapsulation_for_max_speed_when_try_to_assign_raise_attribute_error(race_car):
    # Arrange
    race_car=race_car
    value_error_message_to_max_speed="can't set attribute"
    value_assigning_to_private_variable =5
    
    # Act
    with pytest.raises(Exception) as error:
        race_car.max_speed = value_assigning_to_private_variable
    
    # Assert
    assert  str(error.value) == value_error_message_to_max_speed
    
def test_encapsulation_for_is_engine_started_when_try_to_assign_raise_attribute_error(race_car):
    # Arrange
    race_car=race_car
    value_error_message_to_is_engine_started="can't set attribute"
    value_assigning_to_private_variable=False
    
    # Act
    with pytest.raises(Exception) as error:
        race_car.is_engine_started = value_assigning_to_private_variable
    
    # Assert
    assert  str(error.value) == value_error_message_to_is_engine_started