{"filter":false,"title":"test_get_form_response.py","tooltip":"/ib_miniprojects_backend/essentials_kit_management/tests/presenters/test_get_form_response.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":0},"end":{"row":19,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"a9d0e98a5b9de09819c875ac68045dc7fd716d12","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["import pytest","","from essentials_kit_management.presenters.form_presenter_implementation \\","    import FormPresenterImplementation","","","def test_get_form_response_with_valid_details_return_dict(","        get_form_details_dto,","        get_form_expected_dict):","","    # Arrange","    expected_dict =  get_form_expected_dict","    form_presenter = FormPresenterImplementation()","","    # Act","    actual_dict = form_presenter.get_form_response(get_form_details_dto)","","    # Assert","    assert actual_dict == expected_dict",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["import pytest","","from essentials_kit_management.presenters.form_presenter_implementation \\","    import FormPresenterImplementation","","","def test_get_form_response_with_valid_details_return_dict(","        get_form_details_dto,","        get_form_expected_dict):","","    # Arrange","    expected_dict = get_form_expected_dict","    form_presenter = FormPresenterImplementation()","","    # Act","    actual_dict = form_presenter.get_form_response(get_form_details_dto)","","    # Assert","    assert actual_dict == expected_dict",""]}]]},"timestamp":1591457016088}