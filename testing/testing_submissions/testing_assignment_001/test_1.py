def test_test_1(snapshot):
    variable = [1]
    snapshot.assert_match(variable, "test_1_varialbe")