{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/get_total_reaction_count/api_wrapper.py","undoManager":{"mark":66,"position":66,"stack":[[{"start":{"row":4,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["from django.http import HttpResponse","from fb_post.utils import create_comment","","from raven.utils import json","from fb_post.constants import INVALID_COMMENT_CONTENT","from fb_post.constants import INVALID_POST","","from django_swagger_utils.drf_server.exceptions import BadRequest","from fb_post.validators import InvalidPostException","from fb_post.validators import InvalidCommentContent",""],"id":2}],[{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"remove","lines":["t"],"id":3},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"remove","lines":["n"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"remove","lines":["e"]},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"remove","lines":["m"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"remove","lines":["m"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"remove","lines":["o"]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"remove","lines":["c"]},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":["_"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"remove","lines":["e"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"remove","lines":["t"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"remove","lines":["a"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["e"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["r"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["c"]}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["g"],"id":4},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["e"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":29},"action":"remove","lines":["get"],"id":5},{"start":{"row":5,"column":26},"end":{"row":5,"column":50},"action":"insert","lines":["get_total_reaction_count"]}],[{"start":{"row":8,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["from fb_post.constants import INVALID_COMMENT_CONTENT","from fb_post.constants import INVALID_POST",""],"id":6}],[{"start":{"row":10,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["from fb_post.validators import InvalidPostException","from fb_post.validators import InvalidCommentContent",""],"id":7}],[{"start":{"row":13,"column":0},"end":{"row":34,"column":28},"action":"remove","lines":["    # ---------MOCK IMPLEMENTATION---------","","    try:","        from fb_post.views.get_total_reaction_count.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from fb_post.views.get_total_reaction_count.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from fb_post.views.get_total_reaction_count.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"fb_post\", test_case=test_case,","        operation_name=\"get_total_reaction_count\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":8}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":9}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["t"],"id":10},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["o"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["t"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["a"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["l"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["l"],"id":11},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["a"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["t"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["o"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["t"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["r"],"id":12},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["e"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["a"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["c"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["i"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["o"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["n"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["_"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["c"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["u"],"id":13},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["n"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["t"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["_"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["d"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["i"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["c"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":[" "],"id":14},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["g"],"id":16},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["e"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":29},"action":"remove","lines":["get"],"id":17},{"start":{"row":13,"column":26},"end":{"row":13,"column":50},"action":"insert","lines":["get_total_reaction_count"]}],[{"start":{"row":13,"column":50},"end":{"row":13,"column":52},"action":"insert","lines":["()"],"id":18}],[{"start":{"row":13,"column":52},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["r"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["e"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["s"],"id":20},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["e"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["j"],"id":21},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["s"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["o"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":12},"action":"insert","lines":["    "],"id":22}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":12},"action":"remove","lines":["    "],"id":23}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["n"],"id":24},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["o"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["s"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["j"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["_"],"id":25},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":["n"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["o"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":["i"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["t"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["c"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["a"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["e"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["c"],"id":26},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["o"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["u"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["t"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["n"],"id":27},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["t"]}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["n"],"id":28},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["t"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["_"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["d"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["i"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["c"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["_"],"id":29},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["j"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["s"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["o"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":[" "],"id":30},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["="]}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":[" "],"id":31},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":[" "]}],[{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":[" "],"id":32}],[{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["j"],"id":33},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["o"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["s"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["n"],"id":34},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["s"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["o"]}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["s"],"id":35}],[{"start":{"row":14,"column":22},"end":{"row":14,"column":24},"action":"remove","lines":["js"],"id":36},{"start":{"row":14,"column":22},"end":{"row":14,"column":26},"action":"insert","lines":["json"]}],[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["."],"id":37},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["d"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["j"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["u"]}],[{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["u"],"id":38},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["j"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["u"],"id":39},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["m"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["p"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":32},"end":{"row":14,"column":34},"action":"insert","lines":["()"],"id":40}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":52},"action":"insert","lines":["reaction_count_dict"],"id":41}],[{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"remove","lines":["t"],"id":42},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"remove","lines":["c"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"remove","lines":["i"]},{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"remove","lines":["d"]},{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"remove","lines":["_"]}],[{"start":{"row":14,"column":48},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["r"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["e"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["s"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["p"]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["n"],"id":44},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["s"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":[" "],"id":45},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["H"]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["H"],"id":46},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"remove","lines":[" "]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":[" "],"id":47},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":[" "],"id":48},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":[" "]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["H"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":17},"action":"remove","lines":["Ht"],"id":49},{"start":{"row":15,"column":15},"end":{"row":15,"column":27},"action":"insert","lines":["HttpResponse"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":29},"action":"insert","lines":["()"],"id":50}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":43},"action":"insert","lines":["count_dict_json"],"id":51}],[{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":[","],"id":52},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["s"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["t"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["a"]}],[{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"remove","lines":["a"],"id":53},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"remove","lines":["t"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"remove","lines":["s"]}],[{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":[" "],"id":54},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["s"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["t"]},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["t"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["u"]}],[{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"remove","lines":["u"],"id":55},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["a"],"id":56},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["t"]},{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":["u"]},{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["="],"id":57},{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"insert","lines":["2"]},{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":["0"]},{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":["0"]}],[{"start":{"row":15,"column":56},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["r"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["e"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["t"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["u"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":[" "],"id":59},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["r"]},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["e"]},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["s"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["p"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["n"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"remove","lines":["s"],"id":60},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"remove","lines":["n"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"remove","lines":["p"]},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"remove","lines":["s"]},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"remove","lines":["e"]},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"remove","lines":["r"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"remove","lines":[" "]}],[{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["n"],"id":61}],[{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":[" "],"id":62},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"remove","lines":["s"],"id":63}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["r"],"id":64},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["e"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["s"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["p"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["o"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["n"]},{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":["s"]},{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"remove","lines":["_"],"id":65},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"remove","lines":["n"]},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"remove","lines":["o"]},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"remove","lines":["i"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"remove","lines":["t"]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"remove","lines":["c"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"remove","lines":["a"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["e"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["_"],"id":66},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"insert","lines":["d"]},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"insert","lines":["i"]},{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"insert","lines":["c"]},{"start":{"row":14,"column":42},"end":{"row":14,"column":43},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["o"],"id":67}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":12},"action":"remove","lines":["response"],"id":68},{"start":{"row":15,"column":4},"end":{"row":15,"column":12},"action":"insert","lines":["response"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":36},"end":{"row":4,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588918519942,"hash":"31c2edb7f32982d1707d4bcca7419867580cd5a5"}