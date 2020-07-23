{"changed":true,"filter":false,"title":"tes_get_reactions_to_post_interactor.py","tooltip":"/fb_post_learning/fb_post_v2/tests/interactors/tes_get_reactions_to_post_interactor.py","value":"from unittest.mock import create_autospec\n\nfrom fb_post_v2.interactors.storages import StorageInterface\n\nfrom fb_post_v2.interactors.presenters import PresenterInterface\n\nfrom fb_post_v2.interactors.reply_ import ReplyToCommentInteractor\n\n\nimport pytest\nfrom django_swagger_utils.drf_server.exceptions import NotFound\n\n\ndef test_with_invalid_post_id_raise_exception():\n    # Arrange\n    invalid_post_id = -1\n    user_id = 1\n    comment_content ='New comment'\n    storage = create_autospec(StorageInterface)\n    presenter = create_autospec(PresenterInterface)\n    storage.is_valid_post_id.return_value = False\n    \n    interactor = CreateCommentInteractor(\n        storage=storage,\n        presenter=presenter\n        )\n    presenter.raise_invalid_post_id_exception.side_effect = NotFound\n    # Act\n    with pytest.raises(NotFound):\n        interactor.create_comment(\n            user_id=user_id,\n            post_id=invalid_post_id,\n            comment_content=comment_content\n            )\n\n\ndef test_reply_to_comment_with_invalid_comment_id_raise_exception():\n    \n    # Arrange\n    user_id=1\n    invalid_comment_id = -1\n    reply_content='Replyt Content'\n\n    storage = create_autospec(StorageInterface)\n    presenter = create_autospec(PresenterInterface)\n\n    interactor = ReplyToCommentInteractor(\n        storage=storage,\n        presenter=presenter\n        )\n    storage.is_valid_comment_id.return_value = False\n    presenter.raise_invalid_comment_id_exception.side_effect = NotFound\n\n    # Act\n    with pytest.raises(NotFound):\n        interactor.reply_to_comment(\n            user_id=user_id,\n            comment_id=invalid_comment_id,\n            reply_content=reply_content\n            )\n    # Assert","undoManager":{"mark":-2,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":63,"column":12},"action":"insert","lines":["","from unittest.mock import create_autospec","from fb_post_v2.interactors.storages import \\","    StorageInterface","","from fb_post_v2.interactors.presenters import \\","    PresenterInterface","","from fb_post_v2.interactors.create_comment_interactor import CreateCommentInteractor","from fb_post_v2.interactors.reply_to_comment_interactor import ReplyToCommentInteractor","","","import pytest","from django_swagger_utils.drf_server.exceptions import NotFound","","","def test_with_invalid_post_id_raise_exception():","    # Arrange","    invalid_post_id = -1","    user_id = 1","    comment_content ='New comment'","    storage = create_autospec(StorageInterface)","    presenter = create_autospec(PresenterInterface)","    storage.is_valid_post_id.return_value = False","    ","    interactor = CreateCommentInteractor(","        storage=storage,","        presenter=presenter","        )","    presenter.raise_invalid_post_id_exception.side_effect = NotFound","    # Act","    with pytest.raises(NotFound):","        interactor.create_comment(","            user_id=user_id,","            post_id=invalid_post_id,","            comment_content=comment_content","            )","","","def test_reply_to_comment_with_invalid_comment_id_raise_exception():","    ","    # Arrange","    user_id=1","    invalid_comment_id = -1","    reply_content='Replyt Content'","","    storage = create_autospec(StorageInterface)","    presenter = create_autospec(PresenterInterface)","","    interactor = ReplyToCommentInteractor(","        storage=storage,","        presenter=presenter","        )","    storage.is_valid_comment_id.return_value = False","    presenter.raise_invalid_comment_id_exception.side_effect = NotFound","","    # Act","    with pytest.raises(NotFound):","        interactor.reply_to_comment(","            user_id=user_id,","            comment_id=invalid_comment_id,","            reply_content=reply_content","            )","    # Assert"],"id":1}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "],"id":2},{"start":{"row":2,"column":45},"end":{"row":3,"column":0},"action":"remove","lines":["",""]},{"start":{"row":2,"column":44},"end":{"row":2,"column":45},"action":"remove","lines":["\\"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "],"id":3},{"start":{"row":4,"column":47},"end":{"row":5,"column":0},"action":"remove","lines":["",""]},{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"remove","lines":["\\"]}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["from fb_post_v2.interactors.create_comment_interactor import CreateCommentInteractor",""],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":0,"column":41},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"remove","lines":["r"],"id":7},{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"remove","lines":["o"]},{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"remove","lines":["t"]},{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"remove","lines":["c"]},{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"remove","lines":["a"]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"remove","lines":["r"]},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"remove","lines":["e"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"remove","lines":["t"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"remove","lines":["n"]},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"remove","lines":["i"]},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"remove","lines":["_"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"remove","lines":["t"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":["n"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["e"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["m"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["m"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["o"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["c"],"id":8},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["_"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["o"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":34},"end":{"row":6,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589816555147}