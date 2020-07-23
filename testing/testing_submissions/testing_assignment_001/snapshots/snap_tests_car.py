# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_car_with_snapshot blue_color_car'] = 'Blue'

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_1_color'] = 'Blue'

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_1_maxspeed'] = 30

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_1_tyre_friction'] = 11

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_1_acceleration'] = 12

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_2_color'] = 'White'

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_2_maxspeed'] = 330

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_2_tyre_friction'] = 30

snapshots['test_creating_multiple_car_instances_with_valid_details_snapshot car_2_acceleration'] = 50

snapshots['test_init_function_when_max_speed_is_negative_or_zero_value_raise_exception_snapshot[-1-10-3] Invalid_value_for_max_speed'] = 'Invalid value for max_speed'

snapshots['test_init_function_when_max_speed_is_negative_or_zero_value_raise_exception_snapshot[0-3-10] Invalid_value_for_max_speed'] = 'Invalid value for max_speed'

snapshots['test_init_function_when_tyre_friction_is_negative_or_zero_value_raise_exception[30-10--1] Invalid_value_for_tyre_friction'] = 'Invalid value for tyre_friction'

snapshots['test_init_function_when_tyre_friction_is_negative_or_zero_value_raise_exception[40-10-0] Invalid_value_for_tyre_friction'] = 'Invalid value for tyre_friction'

snapshots['test_encapsulation_for_is_engine_started_when_assign_raise_attribute_snapshot attribute_error_response'] = "can't set attribute"

snapshots['test_start_engine_when_intially_is_at_rest_and_current_speed_zero_snapshot is_engine_started'] = True

snapshots['test_start_engine_when_intially_is_at_rest_and_current_speed_zero_snapshot current_speed'] = 0

snapshots['test_sound_horn_when_car_engine_stopped_return_string_snapshot is_engine_started_response_false'] = False

snapshots['test_sound_horn_when_car_engine_stopped_return_string_snapshot horn_print_statement'] = '''Start the engine to sound_horn
'''

snapshots['test_apply_brakes_with_multiple_times_snapshot current_speed'] = 0

snapshots['test_sound_horn_when_car_engine_started_and_print_beep_beep_snapshot is_engine_started_is_true'] = True

snapshots['test_sound_horn_when_car_engine_started_and_print_beep_beep_snapshot print_statement_beep_beep'] = '''Beep Beep
'''

snapshots['test_with_dictionary dictionary'] = {
    '1': [
        1,
        2,
        3
    ],
    '2': {
        '1': [
            1,
            2,
            3
        ]
    }
}

snapshots['test_test_2 test_2_varialbe'] = [
]
