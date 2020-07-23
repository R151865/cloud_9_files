

import pytest

@pytest.fixture
def truck():
    from truck  import Truck
    color ='Blue'
    max_speed =40
    acceleration=10
    tyre_friction=3
    max_cargo_weight= 150
    
    truck_obj=Truck(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    return truck_obj
    
@pytest.fixture
def truck1():
    from truck import Truck
    max_speed=30
    acceleration=10
    tyre_friction=5
    max_cargo_weight=50
    
    truck_obj=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    return truck_obj



def test_creating_multiple_truck_instances_with_valid_details():
    # Arrange
    from truck  import Truck
    max_speed_1=30
    acceleration_1=12
    tyre_friction_1=11
    color_1='Blue'
    max_cargo_weight_1= 100
    
    max_speed_2=330
    acceleration_2=50
    tyre_friction_2=30
    color_2='White'
    max_cargo_weight_2= 150
    
    # Act
    truck_1=Truck(max_cargo_weight=max_cargo_weight_1,color=color_1,max_speed=max_speed_1,acceleration=acceleration_1,tyre_friction=tyre_friction_1)
    truck_2=Truck(max_cargo_weight=max_cargo_weight_2,color=color_2,max_speed=max_speed_2,acceleration=acceleration_2,tyre_friction=tyre_friction_2)
    
    # Assert
    assert truck_1.color == color_1
    assert truck_1.max_speed ==max_speed_1
    assert truck_1.tyre_friction ==tyre_friction_1
    assert truck_1.acceleration ==acceleration_1
    assert truck_1.max_cargo_weight== max_cargo_weight_1
    
    assert truck_2.color == color_2
    assert truck_2.max_speed ==max_speed_2
    assert truck_2.tyre_friction ==tyre_friction_2
    assert truck_2.acceleration ==acceleration_2
    assert truck_2.max_cargo_weight== max_cargo_weight_2
        
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,color,max_cargo_weight", [
    (50,5,3,'Blue',50),(10,2,1,'Red',100),(100,20,19,'Blue',10),(100,50,1,'White',5)
    ])
def test_create_truck_when_valid_details_given_by_checking_every_attribute(max_cargo_weight,color,max_speed,acceleration,tyre_friction):
    # Arrange
    from truck  import Truck
     
    # Act
    truck=Truck(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    current_speed = 0
    
    # arrange
    assert truck.color == color
    assert truck.max_speed == max_speed
    assert truck.current_speed == current_speed
    assert truck.acceleration == acceleration
    assert truck.tyre_friction == tyre_friction
    assert truck.max_cargo_weight == max_cargo_weight


def test_create_truck_when_color_not_given_return_default_color_blue():
    # Arrange
    from truck  import Truck
    max_speed=40
    acceleration=10
    tyre_friction=3
    max_cargo_weight=200
    default_truck_color_is_blue='Blue'
    
    # Act
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    # Assert
    assert truck.color == default_truck_color_is_blue
    


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(-1,10,3),(0,3,10)])
def test_init_function_when_max_speed_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from truck  import Truck
    
    Invalid_value_for_max_speed='Invalid value for max_speed'
    max_cargo_weight =100
    
    # Act
    with pytest.raises(ValueError) as error:
        truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    # Assert
    assert str(error.value) == Invalid_value_for_max_speed


def test_init_function_when_valid_max_speed_is_given_do_not_raise_error():
    # Arrange
    from truck  import Truck
    max_speed=1
    acceleration=1
    tyre_friction=1
    max_cargo_weight=1
    
    
    # Act
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    # Assert
    assert truck.max_speed == max_speed


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,", [(30,-1,3),(40,0,10)])
def test_init_function_when_acceleration_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from truck  import Truck
    max_cargo_weight=10
    Invalid_value_for_acceleration='Invalid value for acceleration'
     
    # Act
    with pytest.raises(ValueError) as error:
        truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    # Assert
    assert str(error.value) == Invalid_value_for_acceleration
    
    
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [(30,10,-1),(40,10,0)])
def test_init_function_when_tyre_friction_is_negative_or_zero_value_raise_value_error_message(max_speed,acceleration,tyre_friction):
    # Arrange
    from truck  import Truck
    max_cargo_weight =1
    Invalid_value_for_tyre_friction='Invalid value for tyre_friction'
    
    # Act
    with pytest.raises(ValueError) as error:
        truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    # Assert
    assert str(error.value) == Invalid_value_for_tyre_friction


#Task-2

def test_start_engine_is_engine_started_return_true(truck):
    # Arrange
    truck=truck
    is_engine_started=True
    
    # Act
    truck.start_engine()
    
    # Assert
    assert truck.is_engine_started == is_engine_started
    
    
def test_start_engine_when_intially_is_at_rest_and_current_speed_zero(truck):
    # Arrange
    intial_current_speed_of_truck=0
    is_engine_started=True
    
    # Act
    truck.start_engine()
    
    # Assert
    assert truck.is_engine_started== is_engine_started
    assert truck.current_speed == intial_current_speed_of_truck


# Task 3
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed,max_cargo_weight", [
    (30,10,3,20,1),(10,5,5,10,10),(10,6,5,10,100)])
def test_start_engine_whether_displaying_current_speed_after_engine_started_and_accelerated(max_cargo_weight,max_speed, acceleration, tyre_friction,current_speed):
    # Arrange
    from truck  import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    current_speed=current_speed
    is_engine_started=True
    truck.start_engine()
    
    # Act
    truck.accelerate()
    truck.accelerate()
    
    # Assert
    assert truck.is_engine_started == is_engine_started
    assert truck.current_speed == current_speed
    
# Task 4
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed,max_cargo_weight", [
    (30,29,3,29,11),(30,31,1,30,1),(30,30,30,30,10)])
def test_accelerate_when_engine_started_return_current_speed(max_cargo_weight,max_speed, acceleration, tyre_friction,current_speed):
    # Arrange
    from truck  import Truck
    truck_current_speed_after_acceleration=current_speed
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    is_engine_started= True
    truck.start_engine()
    
    # Act
    truck.accelerate()
    
    # Assert
    assert truck.is_engine_started == is_engine_started
    assert truck.current_speed ==  truck_current_speed_after_acceleration
   
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction", [
    (30,29,3),(50,35,1),(10,5,3)
    ])
def test_accelerate_above_max_speed_and_current_speed_is_equal_to_max_speed_only(max_speed, acceleration, tyre_friction):
    # Arrange
    from truck  import Truck
    max_cargo_weight=100
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    truck_max_speed=max_speed
    is_engine_started =True
    truck.start_engine()
    
    # Act
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    
    # Assert
    assert truck.is_engine_started == is_engine_started
    assert truck.current_speed == truck_max_speed

def test_accelerate_when_truck_is_not_started_print_message(truck,capsys):
    # Arrange
    truck=truck
    message_to_start_engine_to_accelerate='Start the engine to accelerate\n'
    is_engine_started=False
    
    # Act
    truck.accelerate()
    output=capsys.readouterr()
    
    # Assert
    assert truck.is_engine_started == is_engine_started
    assert output.out == message_to_start_engine_to_accelerate



def test_stop_engine_when_current_speed_is_not_zero_and_engine_stopped_suddenly_but_current_speed_should_be_not_zero(truck):
    # Arrage
    truck=truck
    truck.start_engine()
    truck.accelerate()
    current_speed_after_engine_stopped=10
    is_engine_started=False
    
    # Act
    truck.stop_engine()
    
    # Assert
    assert truck.is_engine_started == is_engine_started
    assert truck.current_speed == current_speed_after_engine_stopped

def test_start_engine_when_multiple_engine_starts_and_stops_and_accelerates_but_current_should_not_be_zero(truck):
    # Arrange
    truck=truck
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()
    current_speed_after_all=20
    
    # Act
    truck.start_engine()
    truck.accelerate()
    
    # Assert
    assert truck.current_speed == current_speed_after_all
    

# Task-5
@pytest.mark.parametrize("special_case_value,return_value", [
    (-1,0),(0,0),(1,1),(2,2),(-2,0)])
def test_apply_brakes_when_engine_started_with_edge_condition(special_case_value,return_value):
    # Arrange
    from truck  import Truck
    max_speed=40
    acceleration=10
    tyre_friction=4
    color='Blue'
    max_cargo_weight =1
    
    truck=Truck(max_cargo_weight=max_cargo_weight,color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    truck.start_engine()
    
    # Actp
    truck._tyre_friction=0
    truck._current_speed=special_case_value
    truck.apply_brakes()
    
    # Assert
    assert truck.current_speed == return_value
   

  
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed", [
    (30,10,5,5),(40,2,1,1),(40,30,10,20)])
def test_apply_brakes_when_engine_started_and_accelerated_return_current_speed(max_speed,acceleration,tyre_friction,current_speed):
    # Arrage
    from truck  import Truck
    max_cargo_weight =1
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight =max_cargo_weight )
    truck.start_engine()
    truck.accelerate()
    current_speed=current_speed
    is_engine_started = True
    
    # Act
    truck.apply_brakes()
    
    # Assert
    assert truck.is_engine_started == is_engine_started 
    assert truck.current_speed == current_speed
  

def test_apply_brakes_when_engine_is_at_rest_and_not_started_then_current_speed_zero(truck):
    # Arrange
    truck=truck
    current_speed=0
    is_engine_started_is_false= False
    
    # Act
    truck.apply_brakes()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_false
    assert truck.current_speed == current_speed

def test_apply_brakes_with_multiple_times_but_current_speed_should_not_be_negative_value_but_it_should_be_zero_only(truck):
    # Arrange
    truck=truck
    truck.start_engine()
    truck.accelerate()
    current_speed_should_be_zero=0
    
    # Act
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    
    # assert
    assert truck.current_speed == current_speed_should_be_zero
    
def test_apply_brakes_when_current_speed_is_some_value_and_engine_is_started_accelerated_stopped_and_current_speed(truck):
    # Arrange
    truck=truck
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()
    current_speed=7
    is_engine_started_is_false =False
    
    # Act
    truck.apply_brakes()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_false
    assert truck.current_speed == current_speed 


# Task 5
def test_sound_horn_when_truck_engine_started_and_print_beep_beep(truck,capsys):
    # Arrange
    truck=truck
    truck.start_engine()
    honk_honk_sound='Honk Honk\n'
    is_engine_started_is_true=True
    
    # Act
    truck.sound_horn()
    output=capsys.readouterr()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_true
    assert output.out == honk_honk_sound

def test_sound_horn_when_truck_engine_stopped_return_string(truck,capsys):
    # Arrange
    truck=truck
    start_engine_to_sound_horn_string='Start the engine to sound_horn\n'
    is_engine_started_is_false=False
   
    # Act
    truck.sound_horn()
    output=capsys.readouterr()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_false
    assert output.out == start_engine_to_sound_horn_string


# Task -7 
def test_stop_engine_is_engine_started_return_false(truck):
    # Arrange
    truck=truck
    truck.start_engine()
    is_engine_started_is_false=False
    
    # Act
    truck.stop_engine()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_false
    

# Task 8
def test_encapsulation_for_current_speed_when_try_to_assign_raise_attribute_error(truck):
    # Arrange
    truck=truck
    value_error_message_to_current_speed="can't set attribute"
    value_assigning_to_private_variable=0
    
    # Act
    with pytest.raises(Exception) as error:
        truck.current_speed = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) ==  value_error_message_to_current_speed

def test_encapsulation_for_acceleration_when_try_to_assign_raise_attribute_error(truck):
    # Arrange
    truck=truck
    value_error_message_to_acceleration="can't set attribute"
    value_assigning_to_private_variable=5
    
    # Act
    with pytest.raises(Exception) as error:
        truck.acceleration = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) == value_error_message_to_acceleration
    
    
def test_encapsulation_for_color_when_try_to_assign_raise_attribute_error(truck):
    # Arrange
    truck=truck
    value_error_message_to_color="can't set attribute"
    value_assigning_to_private_variable='Black'
    
    # Act
    with pytest.raises(Exception) as error:
        truck.color = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) ==  value_error_message_to_color
    
def test_encapsulation_for_tyre_friction_when_try_to_assign_raise_attribute_error(truck):
    # Arrange
    truck=truck
    value_error_message_to_tyre_friction="can't set attribute"
    value_assigning_to_private_variable =5
    
    # Act   
    with pytest.raises(Exception) as error:
        truck.tyre_friction = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) ==  value_error_message_to_tyre_friction
    
def test_encapsulation_for_max_speed_when_try_to_assign_raise_attribute_error(truck):
    # Arrange
    truck=truck
    value_error_message_to_max_speed="can't set attribute"
    value_assigning_to_private_variable =5
    
    # Act
    with pytest.raises(Exception) as error:
        truck.max_speed = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) == value_error_message_to_max_speed
    
def test_encapsulation_for_is_engine_started_when_try_to_assign_raise_attribute_error(truck):
    # Arrange
    truck=truck
    value_error_message_to_is_engine_started="can't set attribute"
    value_assigning_to_private_variable=False
    
    # Act
    with pytest.raises(Exception) as error:
        truck.is_engine_started = value_assigning_to_private_variable
    
    # Assert
    assert str(error.value) == value_error_message_to_is_engine_started

#max cargo weight



#test max_cargo weight should not be negative or zero or none
@pytest.mark.parametrize('max_cargo_weight',[
    (0),(-1),(-2)
    ])
def test_init_function_when_max_cargo_weight_is_negative_or_zero_or_none_raise_value_error(max_cargo_weight):
    # Arrange
    from truck import Truck
    max_speed=30
    acceleration=10
    tyre_friction=5
    max_cargo_weight=max_cargo_weight
    error_message_for_max_cargo_weight='Invalid value for max_cargo_weight'
    
    # Act
    with pytest.raises(Exception) as error:
        truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(error.value) == error_message_for_max_cargo_weight


def test_init_function_when_max_cargo_weight_value_is_valid_so_do_not_raise_value_error():
    # Arrange
    from truck import Truck
    max_speed=1
    acceleration=1
    tyre_friction=1
    max_cargo_weight=1
    
    # Act
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
   
    # Assert
    assert truck.max_cargo_weight == max_cargo_weight
    

#cargo_weight
#test cargo_weight  should be integer only not be negative or zero or none
@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight',[
    (30,10,1,30,-1),(1,1,1,1,0),(1,1,1,1,-2),(1,1,1,1,-10)
    ])
def test_load_when_cargo_weight_given_negative_or_zero_raise_value_error(max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    error_message_for_max_cargo_weight='Invalid value for cargo_weight'
    
    # Act
    with pytest.raises(Exception) as error:
        truck.load(cargo_weight)
        
    # Assert
    assert str(error.value) == error_message_for_max_cargo_weight

@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight',[
    (30,10,1,30,-1),(1,1,1,1,0),(1,1,1,1,-5)
    ])
def test_unload_when_cargo_weight_given_negative_or_zero_or_none_raise_value_error(max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    error_message_for_max_cargo_weight='Invalid value for cargo_weight'
    
    # Act
    with pytest.raises(Exception) as error:
        truck.unload(cargo_weight)
        
    # Assert
    assert str(error.value) == error_message_for_max_cargo_weight

#load
#test load when after accleration

@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight',[
    (30,10,1,30,1),(1,1,1,1,10),(1,1,1,1,1)
    ])

def test_load_when_truck_engine_started_and_in_motion_result_print_a_statement(capsys,max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    truck.start_engine()
    truck.accelerate()
    cannot_load_during_motion_message='Cannot load cargo during motion\n'
    is_engine_started_is_true =True
    # Act
    truck.load(cargo_weight)
    print_statement=capsys.readouterr()
    
    # Assert
    assert truck.is_engine_started  == is_engine_started_is_true 
    assert str(print_statement.out) == cannot_load_during_motion_message


#load when it is rest only
@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight',[
    (1,1,1,1,1),(1,1,1,10,9)
    ])

def test_load_when_truck_is_in_rest_condition(max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    truck_present_load_weight=cargo_weight
    current_speed =0
    # Act
    truck.load(cargo_weight)
    
    # Assert
    assert truck.current_speed == current_speed
    assert truck.load_weight == truck_present_load_weight


#test load within more than max_cargo_weight should raise print statement
@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight',[
    (1,1,1,1,1),(1,1,1,10,9),(1,1,1,13,7)
    ])
def test_load_when_load_weight_more_than_max_cargo_weight_return_print_statement(capsys,max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    current_speed=0
    cannot_load_cargo_more_than_max_limit_statement='Cannot load cargo more than max limit: {}\n'.format(max_cargo_weight)
    # Act
    truck.load(cargo_weight)
    truck.load(cargo_weight)
    print_statement=capsys.readouterr()
    
    # Assert
    assert truck.current_speed == current_speed
    assert str(print_statement.out) == cannot_load_cargo_more_than_max_limit_statement
    

def test_load_when_truck_engine_started_and_current_speed_is_zero(truck1):
    # Arrange
    truck=truck1
    is_engine_started_is_true= True
    current_speed=0
    load_weight=10
    present_truck_load_weight=20
    truck.start_engine()
    
    # Act
    truck.load(load_weight)
    truck.load(load_weight)
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_true
    assert truck.current_speed == current_speed
    assert truck.load_weight == present_truck_load_weight
    



@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight,current_speed',[
    (10,1,1,10,1,1),(1,10,1,10,3,1),(1,5,1,13,5,1)
    ])
def test_load_when_truck_engine_started_and_current_speed_is_not_zero_print_message(capsys,current_speed,max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    current_speed= current_speed
    cannot_load_during_motion_message='Cannot load cargo during motion\n'
    is_engine_started_is_true=True
    truck.start_engine()
    truck.accelerate()
    
    # Act
    truck.load(cargo_weight)
    print_statement=capsys.readouterr()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_true
    assert truck.current_speed == current_speed
    assert str(print_statement.out) == cannot_load_during_motion_message



def test_load_when_truck_engine_stopped_and_current_speed_is_zero(truck1):
    # Arrange
    truck=truck1
    is_engine_started_is_false= False 
    current_speed=0
    load_weight=10
    present_truck_load_weight=20
    truck.start_engine()
    truck.stop_engine()
    
    # Act
    truck.load(load_weight)
    truck.load(load_weight)
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_false
    assert truck.current_speed == current_speed
    assert truck.load_weight == present_truck_load_weight


@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight',[
    (1,1,1,10,1),(1,1,1,10,3),(1,1,1,13,5)
    ])
def test_load_when_truck_engine_stopped_and_current_speed_is_not_zero_print_message(capsys,max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    cannot_load_during_motion_message='Cannot load cargo during motion\n'
    is_engine_started_is_false=False
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()
    
    # Act
    truck.load(cargo_weight)
    print_statement=capsys.readouterr()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_false
    assert str(print_statement.out) == cannot_load_during_motion_message



# unload
def test_unload_when_load_amount_greater_than_having_amount_then_cargo_weight_should_be_zero_only(truck1):
    # Arrage
    truck=truck1
    unload_amount=30
    present_cargo_weight=0
    current_speed = 0
    # Act
    truck.unload(unload_amount)
    truck.unload(unload_amount)
    truck.unload(unload_amount)
    
    # Arrage
    assert truck.current_speed == current_speed
    assert truck.load_weight == present_cargo_weight
    



@pytest.mark.parametrize('max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight,current_speed',[
    (10,1,1,10,1,1),(1,10,1,10,3,1),(1,5,1,13,5,1)
    ])
def test_unload_when_truck_engine_started_and_current_speed_is_not_zero_print_message(capsys,current_speed,max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
    # Arrange
    from truck import Truck
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    current_speed= current_speed
    cannot_load_during_motion_message='Cannot unload cargo during motion\n'
    is_engine_started_is_true=True
    truck.start_engine()
    truck.accelerate()
    
    # Act
    truck.unload(cargo_weight)
    print_statement=capsys.readouterr()
    
    # Assert
    assert truck.is_engine_started == is_engine_started_is_true
    assert truck.current_speed == current_speed
    assert str(print_statement.out) == cannot_load_during_motion_message



@pytest.mark.parametrize('max_cargo_weight,load_amount,unload_amout,present_load_weight',[
    (10,5,3,4),(30,10,9,2)
    ])

def test_unload_when_truck_is_in_rest_condition_unloaded(max_cargo_weight,load_amount,unload_amout,present_load_weight):
    # Arrange
    from truck import Truck
    max_speed =1
    acceleration =1
    tyre_friction=1
    
    truck=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    current_speed =0
    truck.load(load_amount)
    truck.load(load_amount)
    
    # Act
    truck.unload(unload_amout)
    truck.unload(unload_amout)
    
    
    # Assert
    assert truck.current_speed == current_speed
    assert truck.load_weight == present_load_weight


# encapsulation

def test_encapsulation_of_max_cargo_weight_when_try_to_assign_raise_attribute_error(truck1):
    # Arrange
    truck=truck1
    value_error_message_to_is_max_cargo_weight="can't set attribute"
    assigning_value_to_private_attribute=1
    
    # Act
    with pytest.raises(Exception) as error:
        truck.max_cargo_weight = assigning_value_to_private_attribute
    
    # Assert
    assert str(error.value) == value_error_message_to_is_max_cargo_weight
    
def test_encapsulation_of_load_weight_when_try_to_assign_raise_attribute_error(truck1):
    # Arrange
    truck=truck1
    value_error_message_to_is_load_weight="can't set attribute"
    assigning_value_to_private_attribute=1
    
    # Act
    with pytest.raises(Exception) as error:
        truck.max_cargo_weight = assigning_value_to_private_attribute
    
    # Assert
    assert str(error.value) == value_error_message_to_is_load_weight