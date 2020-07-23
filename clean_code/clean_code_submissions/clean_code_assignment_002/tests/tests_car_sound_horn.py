

# Task 5
def test_sound_horn_when_car_engine_started_and_print_beep_beep(car, capsys):

    # Arrange
    car.start_engine()
    beep_beep_sound = 'Beep Beep\n'

    # Act
    car.sound_horn()

    # Assert
    output = capsys.readouterr()

    assert car.is_engine_started is True
    assert output.out == beep_beep_sound


def test_sound_horn_when_car_engine_stopped_return_string(car, capsys):

    # Arrange
    start_engine_to_sound_horn_string = 'Start the engine to sound_horn\n'

    # Act
    car.sound_horn()

    # Assert
    output = capsys.readouterr()

    assert car.is_engine_started is False
    assert output.out == start_engine_to_sound_horn_string
