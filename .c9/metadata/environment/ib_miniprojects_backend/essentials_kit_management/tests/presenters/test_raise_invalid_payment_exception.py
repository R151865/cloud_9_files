{"filter":false,"title":"test_raise_invalid_payment_exception.py","tooltip":"/ib_miniprojects_backend/essentials_kit_management/tests/presenters/test_raise_invalid_payment_exception.py","undoManager":{"mark":24,"position":24,"stack":[[{"start":{"row":0,"column":0},"end":{"row":22,"column":61},"action":"insert","lines":["import pytest","from essentials_kit_management.presenters.user_presenter_implementation \\","    import UserPresenterImplementation","","from essentials_kit_management.constants.exception_messages import \\","    INVALID_PASSWORD","","from django_swagger_utils.drf_server.exceptions import NotFound","","def test_invalid_password_exception():","","    # Arrange","    exception_message =  INVALID_PASSWORD[0]","    exception_res_status = INVALID_PASSWORD[1]","    user_presenter = UserPresenterImplementation()","","    # Act","    with pytest.raises(NotFound) as exception:","        user_presenter.raise_invalid_password_exception()","","    # Assert","    assert exception.value.message == exception_message","    assert exception.value.res_status == exception_res_status"],"id":1}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":20},"action":"remove","lines":["INVALID_PASSWORD"],"id":2},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["I"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["N"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["V"]}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["A"],"id":3},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["L"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["I"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["D"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["_"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["P"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["A"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["Y"]}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"remove","lines":["Y"],"id":4},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["A"]}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["A"],"id":5},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["Y"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["M"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["E"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["N"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["T"]}],[{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"remove","lines":["n"],"id":6},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"remove","lines":["o"]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"remove","lines":["i"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"remove","lines":["t"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["p"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":["e"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"remove","lines":["c"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"remove","lines":["x"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["e"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["_"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["d"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["r"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["o"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["w"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["s"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"remove","lines":["s"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["a"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["p"],"id":7},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["_"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["d"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["i"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":["l"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["a"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["v"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["n"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["i"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["R"],"id":8},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["A"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["I"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["S"]}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["S"],"id":9},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["I"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["A"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["R"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["r"],"id":10},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["a"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["i"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["s"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["e"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["_"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["i"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["n"],"id":11},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["v"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["l"],"id":12}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["a"],"id":13},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["l"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["i"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["d"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["-"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["p"]}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["p"],"id":14},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["-"]}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["_"],"id":15},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["p"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["a"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["y"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["m"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["e"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["n"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["t"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["_"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["x"],"id":16},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["c"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["e"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["p"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["i"]},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["o"]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["n"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"remove","lines":["t"],"id":17},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"remove","lines":["n"]},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"remove","lines":["o"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"remove","lines":["i"]}],[{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["t"],"id":18},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["i"]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["o"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["n"]}],[{"start":{"row":12,"column":25},"end":{"row":12,"column":41},"action":"remove","lines":["INVALID_PASSWORD"],"id":19},{"start":{"row":12,"column":25},"end":{"row":12,"column":40},"action":"insert","lines":["INVALID_PAYMENT"]}],[{"start":{"row":13,"column":27},"end":{"row":13,"column":43},"action":"remove","lines":["INVALID_PASSWORD"],"id":20},{"start":{"row":13,"column":27},"end":{"row":13,"column":42},"action":"insert","lines":["INVALID_PAYMENT"]}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"remove","lines":["n"],"id":21},{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"remove","lines":["o"]},{"start":{"row":18,"column":52},"end":{"row":18,"column":53},"action":"remove","lines":["i"]},{"start":{"row":18,"column":51},"end":{"row":18,"column":52},"action":"remove","lines":["t"]},{"start":{"row":18,"column":50},"end":{"row":18,"column":51},"action":"remove","lines":["p"]},{"start":{"row":18,"column":49},"end":{"row":18,"column":50},"action":"remove","lines":["e"]},{"start":{"row":18,"column":48},"end":{"row":18,"column":49},"action":"remove","lines":["c"]},{"start":{"row":18,"column":47},"end":{"row":18,"column":48},"action":"remove","lines":["x"]},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"remove","lines":["e"]},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"remove","lines":["_"]},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"remove","lines":["d"]},{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"remove","lines":["r"]},{"start":{"row":18,"column":42},"end":{"row":18,"column":43},"action":"remove","lines":["o"]},{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"remove","lines":["w"]},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"remove","lines":["s"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"remove","lines":["s"]}],[{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"remove","lines":["a"],"id":22},{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"remove","lines":["p"]}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["p"],"id":23},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":["a"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["u"]}],[{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"remove","lines":["u"],"id":24},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"remove","lines":["a"]}],[{"start":{"row":18,"column":23},"end":{"row":18,"column":38},"action":"remove","lines":["raise_invalid_p"],"id":25},{"start":{"row":18,"column":23},"end":{"row":18,"column":54},"action":"insert","lines":["raise_invalid_payment_exception"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":12},"end":{"row":20,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591192995384,"hash":"e8ce08c2cd65cb096bf555acfb196ed03ef0871a"}