

# Task 5
def test_sound_horn_when_race_car_engine_started_and_print_beep_beep(
        race_car, capsys):

    # Arrange
    race_car.start_engine()
    peep_and_beep_sound = 'Peep Peep\nBeep Beep\n'

    # Act
    race_car.sound_horn()

    # Assert
    output = capsys.readouterr()

    assert race_car.is_engine_started is True
    assert output.out == peep_and_beep_sound


def test_sound_horn_when_race_car_engine_stopped_return_string(
        race_car, capsys):

    # Arrange
    start_engine_to_sound_horn_string = 'Start the engine to sound_horn\n'

    # Act
    race_car.sound_horn()

    # Assert
    output = capsys.readouterr()

    assert race_car.is_engine_started is False
    assert output.out == start_engine_to_sound_horn_string
