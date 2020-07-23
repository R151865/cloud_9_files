
"""

Truck test cases
test to create truck with valid data
test to for invalid data for truck

#max cargo weight
test max_cargo weight should not be negative or zero or none

#cargo_weight
test cargo_weight  should be integer only not be negative or zero or none

#load 
test load when after accleration
test load when break_apply
test load when it is in rest only
test load within more than max_cargo_weight should raise print statement
test load when truck engine start and current_speed is zero
test load when truck engine start and current_speed is not zero
test load when engine stop current_speed is not zero
test load when engine stop current_speed is zero
test when truck load is equal to max_cargo_weight exactly,greater,less than edge conditions

#unload 
test unload when huge, load should but load_weight shoudl be zero
test unload when truck engine start and current_speed is zero
test unload when truck engine start and current_speed is not zero
test unload when engine stop current_speed is not zero
test unload when engine stop current_speed is zero
test unload with cargo_weight greater than 
test unload with greater or less or than equal load_weight to load left in the truck
test unload when current_speed is equal to ,less,than,more than, zero
test unload raising error messages

test for encapsulation  

"""
import pytest

@pytest.fixture
def truck():
    from truck import Truck
    max_speed=30
    acceleration=10
    tyre_friction=5
    max_cargo_weight=50
    
    truck_obj=Truck(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    return truck_obj
    

#max cargo weight

#test max_cargo weight should not be negative or zero or none
@pytest.mark.parametrize('max_cargo_weight',[
    (0),(-1),(-2),(None),([]),(2.0)
    ])
def test_max_cargo_weight_when_negative_or_zero_or_none_raise_value_error(max_cargo_weight):
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


def test_max_cargo_weight_value_is_valid_so_do_not_raise_value_error():
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
    (30,10,1,30,-1),(1,1,1,1,0),(1,1,1,1,[]),(1,1,1,1,None)
    ])
def test_cargo_weight_to_load_when_negative_or_zero_or_none_raise_value_error(max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
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
    (30,10,1,30,-1),(1,1,1,1,0),(1,1,1,1,[]),(1,1,1,1,None)
    ])
def test_cargo_weight_to_unload_when_negative_or_zero_or_none_raise_value_error(max_speed,acceleration,tyre_friction,max_cargo_weight,cargo_weight):
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
    

def test_load_when_truck_engine_started_and_current_speed_is_zero(truck):
    # Arrange
    truck=truck
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



def test_load_when_truck_engine_stopped_and_current_speed_is_zero(truck):
    # Arrange
    truck=truck
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
def test_unload_when_load_amount_greater_than_having_amount_then_cargo_weight_should_be_zero_only(truck):
    # Arrage
    truck=truck
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

def test_unload_when_truck_is_in_rest_condition(max_cargo_weight,load_amount,unload_amout,present_load_weight):
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

def test_encapsulation_of_max_cargo_weight_raise_attribute