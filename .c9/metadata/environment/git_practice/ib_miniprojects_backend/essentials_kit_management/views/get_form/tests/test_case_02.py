{"filter":false,"title":"test_case_02.py","tooltip":"/git_practice/ib_miniprojects_backend/essentials_kit_management/views/get_form/tests/test_case_02.py","undoManager":{"mark":15,"position":15,"stack":[[{"start":{"row":0,"column":0},"end":{"row":69,"column":54},"action":"insert","lines":["\"\"\"","# TODO: Get Form","\"\"\"","","import datetime","from essentials_kit_management.utils.custom_utils import CustomTestUtils","from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX","from essentials_kit_management.models.factories import (","    BrandFactory, ItemFactory, SectionFactory, FormFactory,","    OrderFactory","    )","","REQUEST_BODY = \"\"\"","{}","\"\"\"","","TEST_CASE = {","    \"request\": {","        \"path_params\": {\"form_id\": \"1\"},","        \"query_params\": {},","        \"header_params\": {},","        \"securities\": {\"oauth\": {\"tokenUrl\": \"http://auth.ibtspl.com/oauth2/\", \"flow\": \"password\", \"scopes\": [\"read\", \"write\"], \"type\": \"oauth2\"}},","        \"body\": REQUEST_BODY,","    },","}","","","class TestCase01GetFormAPITestCase(CustomTestUtils):","    app_name = APP_NAME","    operation_name = OPERATION_NAME","    request_method = REQUEST_METHOD","    url_suffix = URL_SUFFIX","    test_case_dict = TEST_CASE","","    def setupUser(self, username, password):","        super().setupUser(username=username, password=password)","        self.pop_data()","","    def test_case(self):","        response = self.default_test_case()","","        import json","        response_content = json.loads(response.content)","        self.assert_match_snapshot(name=\"live_form_details\",","                                   value=response_content)","","    def pop_data(self):","        DATE_TIME = datetime.datetime(2000, 10, 10)","","        brands = BrandFactory.create_batch(size=4)","","        items = []","        items.append(ItemFactory(brands=brands[0:2]))","        items.append(ItemFactory(brands=brands[2:4]))","","        sections = []","        sections.append(SectionFactory(items=items))","        sections.append(SectionFactory())","","        form = FormFactory(status=\"LIVE\",","                           close_date=DATE_TIME,","                           expected_delivery_date=DATE_TIME,","                           sections=sections)","","        OrderFactory(form=form, user_id=1,","                     section=sections[0], item=items[0],","                     brand=brands[0], pending_count=0)","        OrderFactory(form=form, user_id=1,","                     section=sections[0], item=items[1],","                     brand=brands[3], pending_count=0)"],"id":1}],[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["m"],"id":2},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["r"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["o"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["F"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":[" "]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["t"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["e"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["G"]}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["I"],"id":3},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["n"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["v"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["a"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["l"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["d"],"id":4}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["i"],"id":5},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":[" "],"id":6},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["F"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["o"],"id":7},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["r"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":[" "],"id":8},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["I"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["1"],"id":9},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":["5"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["4"]},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["3"]},{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":["2"]}],[{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"remove","lines":["2"],"id":10}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":23},"action":"remove","lines":["        self.pop_data()"],"id":11}],[{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"remove","lines":[" "],"id":12},{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"remove","lines":["="]},{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"remove","lines":[" "]},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"remove","lines":["e"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"remove","lines":["s"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"remove","lines":["n"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"remove","lines":["o"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"remove","lines":["p"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"remove","lines":["s"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"remove","lines":["e"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"remove","lines":["r"]}],[{"start":{"row":40,"column":0},"end":{"row":69,"column":54},"action":"remove","lines":["","        import json","        response_content = json.loads(response.content)","        self.assert_match_snapshot(name=\"live_form_details\",","                                   value=response_content)","","    def pop_data(self):","        DATE_TIME = datetime.datetime(2000, 10, 10)","","        brands = BrandFactory.create_batch(size=4)","","        items = []","        items.append(ItemFactory(brands=brands[0:2]))","        items.append(ItemFactory(brands=brands[2:4]))","","        sections = []","        sections.append(SectionFactory(items=items))","        sections.append(SectionFactory())","","        form = FormFactory(status=\"LIVE\",","                           close_date=DATE_TIME,","                           expected_delivery_date=DATE_TIME,","                           sections=sections)","","        OrderFactory(form=form, user_id=1,","                     section=sections[0], item=items[0],","                     brand=brands[0], pending_count=0)","        OrderFactory(form=form, user_id=1,","                     section=sections[0], item=items[1],","                     brand=brands[3], pending_count=0)"],"id":13}],[{"start":{"row":7,"column":0},"end":{"row":10,"column":5},"action":"remove","lines":["from essentials_kit_management.models.factories import (","    BrandFactory, ItemFactory, SectionFactory, FormFactory,","    OrderFactory","    )"],"id":14}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":["1"],"id":15}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["2"],"id":16}]]},"ace":{"folds":[],"scrolltop":360,"scrollleft":0,"selection":{"start":{"row":24,"column":16},"end":{"row":24,"column":16},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":19,"state":"start","mode":"ace/mode/python"}},"timestamp":1593510378905,"hash":"8b9e80985940e9305a5eae19e6302ea15c7ac8b3"}