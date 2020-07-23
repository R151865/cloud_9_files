{"filter":false,"title":"test_update_comment_reaction.py","tooltip":"/fb_post_learning/fb_post_v2/tests/storages/test_update_comment_reaction.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["import pytest","","from fb_post_v2.models import Reaction","","from fb_post_v2.storages.storage_implementation import StorageImplementation","","from fb_post_v2.constants import ReactionTypeEnum","","@pytest.mark.django_db","def test_update_post_reaction_with_valid_details(create_users,","                                                 create_posts,","                                                 create_comments,","                                                 create_reactions):","","    # Arrange","    user_id = 1","    post_id = 1","    reaction_type = ReactionTypeEnum.THUMBS_UP.value","    storage = StorageImplementation()","","    # Act","    storage.update_post_reaction(user_id=user_id,","                                 post_id=post_id,","                                 reaction_type=reaction_type)","","    # Assert","    reaction =  Reaction.objects.get(reacted_by_id=user_id,","                                    post_id=post_id,","                                    reaction=reaction_type)","","    assert user_id == reaction.reacted_by_id","    assert post_id == reaction.post_id","    assert reaction_type == reaction.reaction",""],"id":1}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"remove","lines":["t"],"id":2},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["s"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["o"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["p"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["c"],"id":3},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["o"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["m"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["m"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["e"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["n"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "],"id":4},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":52},"end":{"row":10,"column":53},"action":"remove","lines":[" "],"id":5}],[{"start":{"row":11,"column":52},"end":{"row":11,"column":53},"action":"remove","lines":[" "],"id":6}],[{"start":{"row":12,"column":52},"end":{"row":12,"column":53},"action":"remove","lines":[" "],"id":7}],[{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"remove","lines":["t"],"id":8},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["s"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"remove","lines":["o"]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["c"],"id":9},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["o"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["m"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["m"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["e"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["n"]},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"remove","lines":["t"],"id":10},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"remove","lines":["s"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"remove","lines":["o"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"remove","lines":["p"]}],[{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["c"],"id":11},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["o"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["m"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["m"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["e"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["n"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"remove","lines":["d"],"id":12},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"remove","lines":["i"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"remove","lines":["_"]},{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"remove","lines":["t"]},{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"remove","lines":["s"]},{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"remove","lines":["o"]},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"remove","lines":["p"]}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":36},"action":"insert","lines":["   "],"id":13}],[{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["c"],"id":14},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["o"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["m"]},{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":["m"]},{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"insert","lines":["e"]},{"start":{"row":22,"column":41},"end":{"row":22,"column":42},"action":"insert","lines":["n"]},{"start":{"row":22,"column":42},"end":{"row":22,"column":43},"action":"insert","lines":["t"]},{"start":{"row":22,"column":43},"end":{"row":22,"column":44},"action":"insert","lines":["_"]},{"start":{"row":22,"column":44},"end":{"row":22,"column":45},"action":"insert","lines":["i"]},{"start":{"row":22,"column":45},"end":{"row":22,"column":46},"action":"insert","lines":["d"]}],[{"start":{"row":22,"column":50},"end":{"row":22,"column":51},"action":"remove","lines":["t"],"id":15},{"start":{"row":22,"column":49},"end":{"row":22,"column":50},"action":"remove","lines":["s"]},{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"remove","lines":["o"]},{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"remove","lines":["p"]}],[{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"insert","lines":["c"],"id":16},{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"insert","lines":["o"]},{"start":{"row":22,"column":49},"end":{"row":22,"column":50},"action":"insert","lines":["m"]},{"start":{"row":22,"column":50},"end":{"row":22,"column":51},"action":"insert","lines":["m"]},{"start":{"row":22,"column":51},"end":{"row":22,"column":52},"action":"insert","lines":["e"]},{"start":{"row":22,"column":52},"end":{"row":22,"column":53},"action":"insert","lines":["n"]},{"start":{"row":22,"column":53},"end":{"row":22,"column":54},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":33},"end":{"row":23,"column":36},"action":"insert","lines":["   "],"id":17}],[{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"remove","lines":["t"],"id":18},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"remove","lines":["s"]},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"remove","lines":["o"]},{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"remove","lines":["p"]}],[{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":[" "],"id":19},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["o"]},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["m"]}],[{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"remove","lines":["m"],"id":20},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"remove","lines":["o"]}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["c"],"id":21},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["o"]},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["m"]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["m"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["e"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["n"]},{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":51},"end":{"row":27,"column":52},"action":"remove","lines":["t"],"id":22},{"start":{"row":27,"column":50},"end":{"row":27,"column":51},"action":"remove","lines":["s"]},{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"remove","lines":["o"]},{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"remove","lines":["p"]}],[{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"insert","lines":["o"],"id":23},{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"insert","lines":["c"]}],[{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"remove","lines":["c"],"id":24},{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"remove","lines":["o"]}],[{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"insert","lines":["c"],"id":25},{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"insert","lines":["o"]},{"start":{"row":27,"column":50},"end":{"row":27,"column":51},"action":"insert","lines":["m"]},{"start":{"row":27,"column":51},"end":{"row":27,"column":52},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":51},"end":{"row":27,"column":52},"action":"remove","lines":["e"],"id":26}],[{"start":{"row":27,"column":51},"end":{"row":27,"column":52},"action":"insert","lines":["m"],"id":27},{"start":{"row":27,"column":52},"end":{"row":27,"column":53},"action":"insert","lines":["e"]},{"start":{"row":27,"column":53},"end":{"row":27,"column":54},"action":"insert","lines":["n"]},{"start":{"row":27,"column":54},"end":{"row":27,"column":55},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"insert","lines":[" "],"id":28}],[{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"remove","lines":["d"],"id":29},{"start":{"row":31,"column":36},"end":{"row":31,"column":37},"action":"remove","lines":["i"]},{"start":{"row":31,"column":35},"end":{"row":31,"column":36},"action":"remove","lines":["_"]},{"start":{"row":31,"column":34},"end":{"row":31,"column":35},"action":"remove","lines":["t"]},{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"remove","lines":["s"]},{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"remove","lines":["o"]},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"remove","lines":["p"]}],[{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["c"],"id":30},{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":["o"]},{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["m"]},{"start":{"row":31,"column":34},"end":{"row":31,"column":35},"action":"insert","lines":["m"]},{"start":{"row":31,"column":35},"end":{"row":31,"column":36},"action":"insert","lines":["e"]},{"start":{"row":31,"column":36},"end":{"row":31,"column":37},"action":"insert","lines":["n"]},{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"insert","lines":["t"]},{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":["_"]},{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":["i"]}],[{"start":{"row":31,"column":40},"end":{"row":31,"column":41},"action":"insert","lines":["d"],"id":31}],[{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"remove","lines":["d"],"id":32},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"remove","lines":["i"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"remove","lines":["_"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"remove","lines":["t"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"remove","lines":["s"]},{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"remove","lines":["o"]},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"remove","lines":["p"]}],[{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["c"],"id":33},{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"insert","lines":["o"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["m"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["m"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["e"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["n"]},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["t"]},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"insert","lines":["_"]}],[{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["i"],"id":34},{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["d"]}]]},"ace":{"folds":[],"scrolltop":113.94061979237077,"scrollleft":0,"selection":{"start":{"row":31,"column":44},"end":{"row":31,"column":44},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1589974399912,"hash":"ad2c42c867887fe58fc2689134a7e92ebc456751"}