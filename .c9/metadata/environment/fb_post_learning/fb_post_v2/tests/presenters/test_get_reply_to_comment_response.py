{"filter":false,"title":"test_get_reply_to_comment_response.py","tooltip":"/fb_post_learning/fb_post_v2/tests/presenters/test_get_reply_to_comment_response.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":56},"end":{"row":18,"column":56},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"89cc77c1853488b906c38856337f0b9fc514ee13","undoManager":{"mark":41,"position":41,"stack":[[{"start":{"row":0,"column":0},"end":{"row":17,"column":50},"action":"insert","lines":["from fb_post_v2.presenters import PresenterImplementation","","","def test_get_create_post_response():","","    # Arrange","    post_id = 1","    expected_post_id_dict = {","        \"post_id\": post_id","    }","","    json_presenter = PresenterImplementation()","","    # Act","    actual_post_id = json_presenter.get_create_post_response(post_id=post_id)","","    # Assert","    assert actual_post_id == expected_post_id_dict"],"id":1}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":33},"action":"remove","lines":["get_create_post_response"],"id":3},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["_"]}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["_"],"id":4},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["g"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["e"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["t"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["+"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["+"],"id":5}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["_"],"id":6},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["r"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["e"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["p"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["l"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["y"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["_"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["o"],"id":7},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["c"],"id":8},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["o"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["m"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["m"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["e"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["n"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["t"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["_"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["r"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["s"],"id":9},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["p"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["o"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["n"]},{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":["s"]},{"start":{"row":3,"column":37},"end":{"row":3,"column":38},"action":"insert","lines":["e"]},{"start":{"row":3,"column":38},"end":{"row":3,"column":39},"action":"insert","lines":["_"]},{"start":{"row":3,"column":39},"end":{"row":3,"column":40},"action":"insert","lines":["w"]}],[{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"insert","lines":["i"],"id":10},{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"insert","lines":["t"]},{"start":{"row":3,"column":42},"end":{"row":3,"column":43},"action":"insert","lines":["h"]},{"start":{"row":3,"column":43},"end":{"row":3,"column":44},"action":"insert","lines":["_"]},{"start":{"row":3,"column":44},"end":{"row":3,"column":45},"action":"insert","lines":["v"]},{"start":{"row":3,"column":45},"end":{"row":3,"column":46},"action":"insert","lines":["a"]},{"start":{"row":3,"column":46},"end":{"row":3,"column":47},"action":"insert","lines":["l"]},{"start":{"row":3,"column":47},"end":{"row":3,"column":48},"action":"insert","lines":["i"]},{"start":{"row":3,"column":48},"end":{"row":3,"column":49},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":49},"end":{"row":3,"column":50},"action":"insert","lines":["_"],"id":11},{"start":{"row":3,"column":50},"end":{"row":3,"column":51},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":50},"end":{"row":3,"column":51},"action":"remove","lines":["r"],"id":12}],[{"start":{"row":3,"column":50},"end":{"row":3,"column":51},"action":"insert","lines":["d"],"id":13},{"start":{"row":3,"column":51},"end":{"row":3,"column":52},"action":"insert","lines":["e"]},{"start":{"row":3,"column":52},"end":{"row":3,"column":53},"action":"insert","lines":["t"]},{"start":{"row":3,"column":53},"end":{"row":3,"column":54},"action":"insert","lines":["a"]},{"start":{"row":3,"column":54},"end":{"row":3,"column":55},"action":"insert","lines":["i"]},{"start":{"row":3,"column":55},"end":{"row":3,"column":56},"action":"insert","lines":["l"]},{"start":{"row":3,"column":56},"end":{"row":3,"column":57},"action":"insert","lines":["s"]},{"start":{"row":3,"column":57},"end":{"row":3,"column":58},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":58},"end":{"row":3,"column":59},"action":"insert","lines":["r"],"id":14},{"start":{"row":3,"column":59},"end":{"row":3,"column":60},"action":"insert","lines":["e"]},{"start":{"row":3,"column":60},"end":{"row":3,"column":61},"action":"insert","lines":["t"]},{"start":{"row":3,"column":61},"end":{"row":3,"column":62},"action":"insert","lines":["u"]},{"start":{"row":3,"column":62},"end":{"row":3,"column":63},"action":"insert","lines":["r"]},{"start":{"row":3,"column":63},"end":{"row":3,"column":64},"action":"insert","lines":["n"]},{"start":{"row":3,"column":64},"end":{"row":3,"column":65},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":65},"end":{"row":3,"column":66},"action":"insert","lines":["c"],"id":15},{"start":{"row":3,"column":66},"end":{"row":3,"column":67},"action":"insert","lines":["o"]},{"start":{"row":3,"column":67},"end":{"row":3,"column":68},"action":"insert","lines":["m"]},{"start":{"row":3,"column":68},"end":{"row":3,"column":69},"action":"insert","lines":["m"]},{"start":{"row":3,"column":69},"end":{"row":3,"column":70},"action":"insert","lines":["e"]},{"start":{"row":3,"column":70},"end":{"row":3,"column":71},"action":"insert","lines":["n"]},{"start":{"row":3,"column":71},"end":{"row":3,"column":72},"action":"insert","lines":["t"]},{"start":{"row":3,"column":72},"end":{"row":3,"column":73},"action":"insert","lines":["_"]},{"start":{"row":3,"column":73},"end":{"row":3,"column":74},"action":"insert","lines":["i"]}],[{"start":{"row":3,"column":74},"end":{"row":3,"column":75},"action":"insert","lines":["d"],"id":16}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":11},"action":"remove","lines":["post_id"],"id":17},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["c"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["o"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["m"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["m"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["e"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["n"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["t"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["_"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["i"],"id":18},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"remove","lines":["d"],"id":19},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"remove","lines":["i"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"remove","lines":["_"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["t"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["s"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"remove","lines":["o"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"remove","lines":["p"]}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["c"],"id":20},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["o"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["m"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["m"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["e"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["n"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["t"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["_"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["i"]}],[{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["d"],"id":21}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["t"],"id":22},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["s"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["o"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["c"],"id":23},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["o"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["m"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["m"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["e"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["n"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["_"],"id":24}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["_"],"id":25}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"remove","lines":["d"],"id":26},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["i"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["_"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["t"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["s"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["o"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["c"],"id":27},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["o"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["m"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["m"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["e"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["t"],"id":28},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["_"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["i"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"remove","lines":["e"],"id":29},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"remove","lines":["s"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"remove","lines":["n"]},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"remove","lines":["o"]},{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"remove","lines":["p"]},{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"remove","lines":["s"]},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"remove","lines":["e"]},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"remove","lines":["r"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"remove","lines":["_"]},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"remove","lines":["t"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"remove","lines":["s"]},{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"remove","lines":["o"]},{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"remove","lines":["p"]},{"start":{"row":14,"column":46},"end":{"row":14,"column":47},"action":"remove","lines":["_"]},{"start":{"row":14,"column":45},"end":{"row":14,"column":46},"action":"remove","lines":["e"]},{"start":{"row":14,"column":44},"end":{"row":14,"column":45},"action":"remove","lines":["t"]}],[{"start":{"row":14,"column":43},"end":{"row":14,"column":44},"action":"remove","lines":["a"],"id":30},{"start":{"row":14,"column":42},"end":{"row":14,"column":43},"action":"remove","lines":["e"]},{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":36},"end":{"row":14,"column":41},"action":"remove","lines":["get_c"],"id":31},{"start":{"row":14,"column":36},"end":{"row":14,"column":65},"action":"insert","lines":["get_reply_to_comment_response"]}],[{"start":{"row":14,"column":66},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":15,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":23},"action":"remove","lines":["post_id=post_id"],"id":33},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["c"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["o"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["m"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["m"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["e"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["n"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["t"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["_"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["i"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["="],"id":34},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["c"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["o"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["m"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["m"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["e"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["n"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["_"],"id":35},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["i"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["t"],"id":36},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["s"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["o"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["c"],"id":37},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["o"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["m"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["m"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["e"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["n"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"remove","lines":["t"],"id":38},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"remove","lines":["s"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"remove","lines":["o"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"remove","lines":["p"]}],[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["c"],"id":39},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":23},"action":"remove","lines":["actual_co_id"],"id":40},{"start":{"row":18,"column":11},"end":{"row":18,"column":28},"action":"insert","lines":["actual_comment_id"]}],[{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"remove","lines":["t"],"id":41},{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"remove","lines":["s"]},{"start":{"row":18,"column":42},"end":{"row":18,"column":43},"action":"remove","lines":["o"]},{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"remove","lines":["p"]}],[{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":["c"],"id":42},{"start":{"row":18,"column":42},"end":{"row":18,"column":43},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":32},"end":{"row":18,"column":51},"action":"remove","lines":["expected_co_id_dict"],"id":43},{"start":{"row":18,"column":32},"end":{"row":18,"column":56},"action":"insert","lines":["expected_comment_id_dict"]}]]},"timestamp":1590407156712}