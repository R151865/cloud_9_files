{"filter":false,"title":"test_get_user_ordered_details_interactor.py","tooltip":"/ib_miniprojects_backend/essentials_kit_management/tests/interactors/test_get_user_ordered_details_interactor.py","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":2}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":50,"column":60},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":51,"column":0},"end":{"row":51,"column":9},"action":"insert","lines":["         "]}],[{"start":{"row":51,"column":8},"end":{"row":51,"column":9},"action":"remove","lines":[" "],"id":5},{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["    "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":51,"column":0},"end":{"row":52,"column":0},"action":"remove","lines":["",""],"id":6}],[{"start":{"row":0,"column":0},"end":{"row":51,"column":0},"action":"remove","lines":["import pytest","","from unittest.mock import create_autospec","","from django_swagger_utils.drf_server.exceptions import NotFound","","from essentials_kit_management.interactors.presenters import \\","    FormPresenterInterface","from essentials_kit_management.interactors.storages import \\","    FormStorageInterface","","from essentials_kit_management.interactors.get_user_ordered_details_interactor \\","    import GetUserOrderedDetailsInteractor","","from essentials_kit_management.interactors.storages.dtos import (","    GetUserOrderDto",")","","","def test_get_user_ordered_details_interactor_with_valid_details(","        get_user_brand_dtos,","        get_user_items_dtos,","        get_user_order_dtos,","        get_expected_get_user_order_dtos","):","","    # Arrange","    user_id = 1","    form_id = 1","    expected_dict = {}","    form_presenter = create_autospec(FormPresenterInterface)","    form_storage = create_autospec(FormStorageInterface)","    interactor = GetUserOrderedDetailsInteractor(form_storage=form_storage,","                                                 form_presenter=form_presenter)","","    form_storage.get_order_dtos.return_value = get_user_order_dtos","    form_storage.get_user_brand_dtos.return_value = get_user_brand_dtos","    form_storage.get_user_item_dtos.return_value = get_user_items_dtos","","    # Act","    actual_dict = interactor.get_user_ordered_details(user_id=user_id,","                                                      form_id=form_id)","","    # Assert","    form_storage.is_valid_form_id(form_id=form_id)","    form_storage.get_order_dtos.assert_called_once_with(user_id=user_id,","                                                        form_id=form_id)","    form_storage.get_user_brand_dtos.assert_called_once()","    form_storage.get_user_item_dtos.assert_called_once()","    form_presenter.get_user_ordered_details_response(","         order_detail_dtos=get_expected_get_user_order_dtos)",""],"id":7},{"start":{"row":0,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["import pytest","","from unittest.mock import create_autospec","","from django_swagger_utils.drf_server.exceptions import NotFound","","from essentials_kit_management.interactors.presenters import \\","    FormPresenterInterface","from essentials_kit_management.interactors.storages import \\","    FormStorageInterface","","from essentials_kit_management.interactors. \\","    get_user_ordered_details_interactor import GetUserOrderedDetailsInteractor","","from essentials_kit_management.interactors.storages.dtos import (","    GetUserOrderDto",")","","","def test_get_user_ordered_details_interactor_with_valid_details(","        get_user_brand_dtos,","        get_user_items_dtos,","        get_user_order_dtos,","        get_expected_get_user_order_dtos","):","","    # Arrange","    user_id = 1","    form_id = 1","    expected_dict = {}","    form_presenter = create_autospec(FormPresenterInterface)","    form_storage = create_autospec(FormStorageInterface)","    interactor = GetUserOrderedDetailsInteractor(form_storage=form_storage,","                                                 form_presenter=form_presenter)","","    form_storage.get_order_dtos.return_value = get_user_order_dtos","    form_storage.get_user_brand_dtos.return_value = get_user_brand_dtos","    form_storage.get_user_item_dtos.return_value = get_user_items_dtos","","    # Act","    actual_dict = interactor.get_user_ordered_details(user_id=user_id,","                                                      form_id=form_id)","","    # Assert","    form_storage.is_valid_form_id(form_id=form_id)","    form_storage.get_order_dtos.assert_called_once_with(user_id=user_id,","                                                        form_id=form_id)","    form_storage.get_user_brand_dtos.assert_called_once()","    form_storage.get_user_item_dtos.assert_called_once()","    form_presenter.get_user_ordered_details_response(","         order_detail_dtos=get_expected_get_user_order_dtos)",""]}]]},"ace":{"folds":[],"scrolltop":360,"scrollleft":0,"selection":{"start":{"row":51,"column":0},"end":{"row":51,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":21,"state":"start","mode":"ace/mode/python"}},"timestamp":1591454581410,"hash":"79ea2fa48bff1f1d7e053bf1d93f471726db6595"}