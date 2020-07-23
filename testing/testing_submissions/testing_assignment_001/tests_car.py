import pytest

@pytest.fixture
def car():
    from car import Car
    car_obj=Car(color='Blue',max_speed=40,acceleration=10,tyre_friction=3)
    return car_obj

"""
# Task-1 Creating car
def test_creating_multiple_car_instances_with_valid_details():
    # Arrange
    from car import Car
    max_speed_1=30
    acceleration_1=12
    tyre_friction_1=11
    color_1='Blue'

    max_speed_2=330
    acceleration_2=50
    tyre_friction_2=30
    color_2='White'
    
    # Act
    car_1=Car(color=color_1,max_speed=max_speed_1,acceleration=acceleration_1,tyre_friction=tyre_friction_1)
    car_2=Car(color=color_2,max_speed=max_speed_2,acceleration=acceleration_2,tyre_friction=tyre_friction_2)
    
    # Assert
    assert car_1.color == color_1
    assert car_1.max_speed ==max_speed_1
    assert car_1.tyre_friction ==tyre_friction_1
    assert car_1.acceleration ==acceleration_1
    
    assert car_2.color == color_2
    assert car_2.max_speed ==max_speed_2
    assert car_2.tyre_friction ==tyre_friction_2
    assert car_2.acceleration ==acceleration_2


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,color", [
    (50,5,3,'Blue'),(10,2,1,'Red'),(100,20,19,'Blue'),(100,50,1,'White')
    ])
def test_create_car_when_valid_details_given_by_checking_every_attribute(color,max_speed,acceleration,tyre_friction):
    # Arrange
    from car import Car 
     
    # Act
    car=Car(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    current_speed = 0
    
    # arrange
    assert car.color == color
    assert car.max_speed == max_speed
    assert car.current_speed == current_speed
    assert car.acceleration == acceleration
    assert car.tyre_friction == tyre_friction


def test_create_car_when_color_not_given_return_default_color_blue():
    # Arrange
    from car import Car
    max_speed=40
    acceleration=10
    tyre_friction=3
    default_car_color_is_blue='Blue'
    
    # Act
    car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert car.color == default_car_color_is_blue



@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(-1,10,3),(0,3,10)])
def test_init_function_when_max_speed_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from car import Car
    
    Invalid_value_for_max_speed='Invalid value for max_speed'
    
    # Act
    with pytest.raises(ValueError) as e:
        car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert str(e.value) == Invalid_value_for_max_speed


def test_init_function_when_valid_max_speed_is_given_do_not_raise_error():
    # Arrange
    from car import Car
    max_speed=1
    acceleration=1
    tyre_friction=1
    
    
    # Act
    car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert car.max_speed == max_speed


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(30,-1,3),(40,0,10)])
def test_init_function_when_acceleration_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from car import Car
    Invalid_value_for_acceleration='Invalid value for acceleration'
    # Act
    with pytest.raises(ValueError) as e:
        car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert str(e.value) == Invalid_value_for_acceleration
    
    
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(30,10,-1),(40,10,0)])
def test_init_function_when_tyre_friction_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from car import Car
    Invalid_value_for_tyre_friction='Invalid value for tyre_friction'
    
    # Act
    with pytest.raises(ValueError) as e:
        car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    assert str(e.value) == Invalid_value_for_tyre_friction


#Task-2

def test_start_engine_is_engine_started_return_true(car):
    # Arrange
    car=car
    is_engine_started=True
    
    # Act
    car.start_engine()
    
    # Assert
    assert car.is_engine_started == is_engine_started
    
    
def test_start_engine_when_intially_is_at_rest_and_current_speed_zero(car):
    # Arrange
    intial_current_speed_of_car=0
    is_engine_started=True
    
    # Act
    car.start_engine()
    
    # Assert
    assert car.is_engine_started== is_engine_started
    assert car.current_speed == intial_current_speed_of_car


# Task 3
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed", [
    (30,10,3,20),(10,5,5,10),(10,6,5,10)])
def test_start_engine_when_engine_started_and_accelerated_display_car_speed(max_speed, acceleration, tyre_friction,current_speed):
    # Arrange
    from car import Car
    car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    current_speed=current_speed
    is_engine_started=True
    car.start_engine()
    
    # Act
    car.accelerate()
    car.accelerate()
    
    # Assert
    assert car.is_engine_started == is_engine_started
    assert car.current_speed == current_speed
    
# Task 4
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed", [
    (30,29,3,29),(30,31,1,30),(30,30,30,30)])
def test_accelerate_when_engine_started_return_current_speed(max_speed, acceleration, tyre_friction,current_speed):
    # Arrange
    from car import Car
    car_current_speed_after_acceleration=current_speed
    car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    is_engine_started= True
    car.start_engine()
    
    # Act
    car.accelerate()
    
    # Assert
    assert car.is_engine_started == is_engine_started
    assert car.current_speed ==  car_current_speed_after_acceleration
   
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [
    (30,29,3),(50,35,1),(10,5,3)
    ])
def test_accelerate_above_max_speed_and_current_speed_is_equal_to_max_speed_only(max_speed, acceleration, tyre_friction):
    # Arrange
    from car import Car
    car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    car_max_speed=max_speed
    is_engine_started =True
    car.start_engine()
    
    # Act
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    
    # Assert
    assert car.is_engine_started == is_engine_started
    assert car.current_speed == car_max_speed

def test_accelerate_when_car_is_not_started_print_message(car,capsys):
    # Arrange
    car=car
    message_to_start_engine_to_accelerate='Start the engine to accelerate\n'
    is_engine_started=False
    
    # Act
    car.accelerate()
    output=capsys.readouterr()
    
    # Assert
    assert car.is_engine_started == is_engine_started
    assert output.out == message_to_start_engine_to_accelerate



def test_stop_engine_when_current_speed_is_not_zero_and_engine_stopped_suddenly_then_current_speed_should_be_not_zero(car):
    # Arrage
    car=car
    car.start_engine()
    car.accelerate()
    current_speed_after_engine_stopped=10
    is_engine_started=False
    
    # Act
    car.stop_engine()
    
    # Assert
    assert car.is_engine_started == is_engine_started
    assert car.current_speed == current_speed_after_engine_stopped

def test_start_engine_when_multiple_engine_starts_and_stops_but_current_speed_should_not_be_zero(car):
    # Arrange
    car=car
    car.start_engine()
    car.accelerate()
    car.stop_engine()
    current_speed_after_all=20
    
    # Act
    car.start_engine()
    car.accelerate()
    
    # Assert
    assert car.current_speed == current_speed_after_all
    

# Task-5

@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed", [
    (30,10,5,5),(40,2,1,1),(40,30,10,20)])
def test_apply_brakes_when_engine_started_and_accelerated_return_current_speed(max_speed,acceleration,tyre_friction,current_speed):
    # Arrage
    from car import Car
    car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    car.start_engine()
    car.accelerate()
    current_speed=current_speed
    is_engine_started = True
    
    # Act
    car.apply_brakes()
    
    # Assert
    assert car.is_engine_started == is_engine_started 
    assert car.current_speed == current_speed
  

def test_apply_brakes_when_engine_is_at_rest_and_not_started_then_current_speed_zero(car):
    # Arrange
    car=car
    current_speed=0
    is_engine_started_is_false= False
    
    # Act
    car.apply_brakes()
    
    # Assert
    assert car.is_engine_started == is_engine_started_is_false
    assert car.current_speed == current_speed

def test_apply_brakes_with_multiple_times_but_current_speed_should_not_be_negative_value_but_it_should_be_zero_only(car):
    # Arrange
    car=car
    car.start_engine()
    car.accelerate()
    current_speed_should_be_zero=0
    
    # Act
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    
    # assert
    assert car.current_speed == current_speed_should_be_zero
    
def test_apply_brakes_when_current_speed_is_some_value_and_engine_is_started_accelerated_stopped_and_current_speed(car):
    # Arrange
    car=car
    car.start_engine()
    car.accelerate()
    car.stop_engine()
    current_speed=7
    is_engine_started_is_false =False
    
    # Act
    car.apply_brakes()
    
    # Assert
    assert car.is_engine_started == is_engine_started_is_false
    assert car.current_speed == current_speed 


# Task 5
def test_sound_horn_when_car_engine_started_and_print_beep_beep(car,capsys):
    # Arrange
    car=car
    car.start_engine()
    Beep_Beep_sound='Beep Beep\n'
    is_engine_started_is_true=True
    
    # Act
    car.sound_horn()
    output=capsys.readouterr()
    
    # Assert
    assert car.is_engine_started == is_engine_started_is_true
    assert output.out == Beep_Beep_sound


def test_sound_horn_when_car_engine_stopped_return_string(car,capsys):
    # Arrange
    car=car
    start_engine_to_sound_horn_string='Start the engine to sound_horn\n'
    is_engine_started_is_false=False
   
    # Act
    car.sound_horn()
    output=capsys.readouterr()
    
    # Assert
    assert car.is_engine_started == is_engine_started_is_false
    assert output.out == start_engine_to_sound_horn_string


# Task -7 
def test_stop_engine_is_engine_started_return_false(car):
    # Arrange
    car=car
    car.start_engine()
    is_engine_started_is_false=False
    
    # Act
    car.stop_engine()
    
    # Assert
    assert car.is_engine_started == is_engine_started_is_false

# Task 8
def test_encapsulation_for_current_speed_when_assign_raise_attribute_error(car):
    # Arrange
    car=car
    value_error_message_to_current_speed="can't set attribute"
    value_assigning_to_private_variable=0
    
    # Act
    with pytest.raises(Exception) as error:
        car.current_speed = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) ==  value_error_message_to_current_speed

def test_encapsulation_for_acceleration_when_assign_raise_attribute_error(car):
    # Arrange
    car=car
    value_error_message_to_acceleration="can't set attribute"
    value_assigning_to_private_variable=5
    
    # Act
    with pytest.raises(Exception) as error:
        car.acceleration = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) == value_error_message_to_acceleration
    
    
def test_encapsulation_for_color_when_assign_raise_attribute_error(car):
    # Arrange
    car=car
    value_error_message_to_color="can't set attribute"
    value_assigning_to_private_variable='Black'
    
    # Act
    with pytest.raises(Exception) as error:
        car.color = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) ==  value_error_message_to_color
    
def test_encapsulation_for_tyre_friction_when_assign_raise_attribute_error(car):
    # Arrange
    car=car
    value_error_message_to_tyre_friction="can't set attribute"
    value_assigning_to_private_variable =5
    
    # Act   
    with pytest.raises(Exception) as error:
        car.tyre_friction = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) ==  value_error_message_to_tyre_friction
    
def test_encapsulation_for_max_speed_when_assign_raise_attribute_error(car):
    # Arrange
    car=car
    value_error_message_to_max_speed="can't set attribute"
    value_assigning_to_private_variable =5
    
    # Act
    with pytest.raises(Exception) as error:
        car.max_speed = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) == value_error_message_to_max_speed
    
def test_encapsulation_for_is_engine_started_when_assign_raise_attribute_error(car):
    # Arrange
    car=car
    value_error_message_to_is_engine_started="can't set attribute"
    value_assigning_to_private_variable=False
    
    # Act
    with pytest.raises(Exception) as error:
        car.is_engine_started = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) == value_error_message_to_is_engine_started
"""



def test_create_car_with_snapshot(snapshot):

    # Arrange
    from car import Car
    max_speed=40
    acceleration=10
    tyre_friction=3
    default_car_color_is_blue='Blue'

    # Act
    car=Car(max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction)

    # Assert
    car_color = car.color
    snapshot.assert_match(car_color, "blue_color_car")

def test_creating_multiple_car_instances_with_valid_details_snapshot(snapshot):

    # Arrange
    from car import Car
    max_speed_1=30
    acceleration_1=12
    tyre_friction_1=11
    color_1='Blue'

    max_speed_2=330
    acceleration_2=50
    tyre_friction_2=30
    color_2='White'

    # Act
    car_1=Car(color=color_1,max_speed=max_speed_1,acceleration=acceleration_1,tyre_friction=tyre_friction_1)
    car_2=Car(color=color_2,max_speed=max_speed_2,acceleration=acceleration_2,tyre_friction=tyre_friction_2)

    # Assert
    assert car_1.color == color_1
    assert car_1.max_speed ==max_speed_1
    assert car_1.tyre_friction ==tyre_friction_1
    assert car_1.acceleration ==acceleration_1

    assert car_2.color == color_2
    assert car_2.max_speed ==max_speed_2
    assert car_2.tyre_friction ==tyre_friction_2
    assert car_2.acceleration ==acceleration_2

    snapshot.assert_match(car_1.color, "car_1_color")
    snapshot.assert_match(car_1.max_speed, "car_1_maxspeed")
    snapshot.assert_match(car_1.tyre_friction, "car_1_tyre_friction")
    snapshot.assert_match(car_1.acceleration, "car_1_acceleration")

    snapshot.assert_match(car_2.color, "car_2_color")
    snapshot.assert_match(car_2.max_speed, "car_2_maxspeed")
    snapshot.assert_match(car_2.tyre_friction, "car_2_tyre_friction")
    snapshot.assert_match(car_2.acceleration, "car_2_acceleration")

@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(-1,10,3),(0,3,10)])
def test_init_function_when_max_speed_is_negative_or_zero_value_raise_exception_snapshot(
        snapshot,
        max_speed,
        acceleration,
        tyre_friction
):
    # Arrange
    from car import Car

    # Act
    with pytest.raises(ValueError) as e:
        car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    # Assert
    error_message = str(e.value)
    snapshot.assert_match(error_message, "Invalid_value_for_max_speed")

@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(30,10,-1),(40,10,0)])
def test_init_function_when_tyre_friction_is_negative_or_zero_value_raise_exception(
        snapshot,
        max_speed,
        acceleration,
        tyre_friction
):
    # Arrange
    from car import Car

    # Act
    with pytest.raises(ValueError) as e:
        car=Car(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)

    # Assert
    error_message = str(e.value)
    snapshot.assert_match(error_message, "Invalid_value_for_tyre_friction")


def test_encapsulation_for_is_engine_started_when_assign_raise_attribute_snapshot(
        snapshot,
        car
):
    # Arrange
    value_assigning_to_private_variable=False

    # Act
    with pytest.raises(Exception) as error:
        car.is_engine_started = value_assigning_to_private_variable

    # Assert
    error_message = str(error.value)
    snapshot.assert_match(error_message, "attribute_error_response")

def test_start_engine_when_intially_is_at_rest_and_current_speed_zero_snapshot(
    snapshot,
    car
):
    # Arrange
    # Act
    car.start_engine()

    # Assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")

def test_sound_horn_when_car_engine_stopped_return_string_snapshot(
        snapshot,
        car,
        capsys
):
    # Arrange
    # Act
    car.sound_horn()
    output=capsys.readouterr()
    
    # Assert
    snapshot.assert_match(car.is_engine_started,
                          "is_engine_started_response_false")
    snapshot.assert_match(output.out,
                          "horn_print_statement")

def test_apply_brakes_with_multiple_times_snapshot(snapshot, car):
    # Arrange
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # assert
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Assert
    snapshot.assert_match(car.current_speed, "current_speed")


def test_sound_horn_when_car_engine_started_and_print_beep_beep_snapshot(
        snapshot,
        car,
        capsys
):
    # Arrange
    car.start_engine()

    # Act
    car.sound_horn()
    output=capsys.readouterr()

    # Assert
    snapshot.assert_match(car.is_engine_started , "is_engine_started_is_true")
    snapshot.assert_match(output.out, "print_statement_beep_beep")


def test_with_dictionary(snapshot):
    dictionary = {
        "1": [1, 2, 3],
        "2": {
            "1" : [1, 2, 3]
        }
    }
    snapshot.assert_match(dictionary, "dictionary")

def test_test_2(snapshot):
    variable = []
    snapshot.assert_match(variable, "test_2_varialbe")