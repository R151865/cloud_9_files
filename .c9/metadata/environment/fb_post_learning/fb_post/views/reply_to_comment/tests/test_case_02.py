{"filter":false,"title":"test_case_02.py","tooltip":"/fb_post_learning/fb_post/views/reply_to_comment/tests/test_case_02.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":40,"column":41},"action":"insert","lines":["\"\"\"","# TODO: Update test case description","\"\"\"","","from django_swagger_utils.utils.test import CustomAPITestCase","from fb_post.utils.custom_test_utils_2 import CustomTestUtils","from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX","","REQUEST_BODY = \"\"\"","{","    \"content\": \"\"","}","\"\"\"","","TEST_CASE = {","    \"request\": {","        \"path_params\": {\"comment_id\": \"1234\"},","        \"query_params\": {},","        \"header_params\": {},","        \"securities\": {\"oauth\": {\"tokenUrl\": \"http://auth.ibtspl.com/oauth2/\", \"flow\": \"password\", \"scopes\": [\"superuser\"], \"type\": \"oauth2\"}},","        \"body\": REQUEST_BODY,","    },","}","","","class TestCase01ReplyToCommentAPITestCase(CustomTestUtils):","    app_name = APP_NAME","    operation_name = OPERATION_NAME","    request_method = REQUEST_METHOD","    url_suffix = URL_SUFFIX","    test_case_dict = TEST_CASE","","    def setupUser(self, username, password):","        super(TestCase01ReplyToCommentAPITestCase, self).setupUser(","            username=username, password=password","        )","","    def test_case(self):","        self.default_test_case() # Returns response object.","        # Which can be used for further response object checks.","        # Add database state checks here."],"id":1}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["s"],"id":2},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["r"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"remove","lines":["r"],"id":3},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"remove","lines":["r"]}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["t"],"id":4},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["r"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["i"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["n"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["g"]}],[{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"remove","lines":["n"],"id":5},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"remove","lines":["o"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"remove","lines":["i"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":["t"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["p"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"remove","lines":["i"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"remove","lines":["r"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"remove","lines":["c"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["s"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"remove","lines":["e"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":["d"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":[" "]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["e"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["s"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["a"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["c"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":[" "]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["t"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["s"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["e"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["t"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":[" "]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["t"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":["a"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["d"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["p"]}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["U"],"id":6}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["C"],"id":7},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["r"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["e"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["a"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["t"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["C"],"id":8},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["o"],"id":9},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["C"]}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["R"],"id":10},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["e"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["p"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["l"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["y"]}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["y"],"id":11},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["l"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["p"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["e"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["R"]}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":[" "],"id":12},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["R"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["e"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["p"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["l"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["y"]}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["y"],"id":13},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["l"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["p"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["e"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["R"]}],[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["Y"],"id":14}],[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["Y"],"id":15}],[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["T"],"id":16},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":[" "],"id":17},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["C"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["o"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["m"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["m"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["e"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["n"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["h"],"id":19},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["a"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"remove","lines":["n"],"id":20},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["a"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"remove","lines":["h"]}],[{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["H"],"id":21},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["a"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["n"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["d"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["l"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["i"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["g"],"id":22}],[{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":[" "],"id":23},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["C"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["o"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["m"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["m"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["e"]},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":["t"],"id":24}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"remove","lines":["t"],"id":25},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"remove","lines":["n"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"remove","lines":["e"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"remove","lines":["m"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"remove","lines":["m"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"remove","lines":["o"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"remove","lines":["C"]}],[{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["I"],"id":26},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["n"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["v"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["a"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["l"]},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["i"]},{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":["d"]},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["C"]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["o"],"id":27}],[{"start":{"row":1,"column":35},"end":{"row":1,"column":44},"action":"remove","lines":["InvalidCo"],"id":28},{"start":{"row":1,"column":35},"end":{"row":1,"column":58},"action":"insert","lines":["InvalidCommentException"]}],[{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"remove","lines":[" "],"id":29}],[{"start":{"row":38,"column":32},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":39,"column":0},"end":{"row":39,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["1"],"id":31}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["2"],"id":32}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":24},"action":"remove","lines":["1"],"id":33}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":24},"action":"insert","lines":["2"],"id":34}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":41,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1592976524261,"hash":"9a7f267c7d1c67d02a00ddbf04aff48d91c7f048"}