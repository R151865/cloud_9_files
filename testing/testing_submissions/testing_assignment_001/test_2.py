def test_test_2(snapshot):
    variable = [2]
    snapshot.assert_match(variable, "test_2_varialbe")

def test_test_3(snapshot):
    variable = []
    snapshot.assert_match(variable, "test_3_varialbe")