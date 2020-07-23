{"filter":false,"title":"user_auth_service.py","tooltip":"/git_practice/ib_miniprojects_backend/auth_service/adapters/user_auth_service.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":31},"end":{"row":9,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"e6a0be5f7c0a85c5451a564661bee1034d3adeb8","undoManager":{"mark":75,"position":75,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["from typing import List","","","class AuthService:","    @property","    def interface(self):","        from fb_post_auth.interfaces.service_interface import ServiceInterface","        return ServiceInterface()","","    def get_user_dtos(self, user_ids: List[int]):","        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)","","        # TODO: Convert to DTO in this app","        return user_dtos",""],"id":1}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["from typing import List",""],"id":3},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["U"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["s"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["e"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["r"],"id":4},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["e"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["s"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["U"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["c"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["l"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["a"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["s"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":[" "],"id":6},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["U"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["s"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["r"],"id":7},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["A"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["u"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["t"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["h"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["S"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["e"],"id":8},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["r"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["v"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["i"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["c"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["e"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":[":"]}],[{"start":{"row":2,"column":22},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["@"],"id":10},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["p"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["r"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["o"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["p"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["e"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["r"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["t"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["y"]}],[{"start":{"row":3,"column":13},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["d"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["e"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":[" "],"id":12},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["i"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["n"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["t"]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["e"]},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["f"],"id":13},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["a"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["c"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":19},"action":"insert","lines":["()"],"id":14}],[{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["s"],"id":15},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["e"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["l"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["f"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["k"]}],[{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"remove","lines":["k"],"id":16}],[{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":[":"],"id":17}],[{"start":{"row":4,"column":24},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":5,"column":0},"end":{"row":5,"column":8},"action":"insert","lines":["        "]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"remove","lines":["d"],"id":19}],[{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["f"],"id":20},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["r"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["o"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["m"]}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":[" "],"id":21},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["c"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["o"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["m"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["m"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["o"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["n"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["."]}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["i"],"id":22},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["n"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["t"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["e"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["r"],"id":23},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["e"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["t"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["n"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["i"]}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["s"],"id":24},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["e"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":23},"action":"remove","lines":["ser"],"id":25},{"start":{"row":5,"column":20},"end":{"row":5,"column":37},"action":"insert","lines":["service_interface"]}],[{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["."],"id":26}],[{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"remove","lines":["."],"id":27}],[{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":[" "],"id":28},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["i"]},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["m"]},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["p"]},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"insert","lines":["o"]},{"start":{"row":5,"column":42},"end":{"row":5,"column":43},"action":"insert","lines":["r"]},{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":44},"end":{"row":5,"column":45},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":5,"column":45},"end":{"row":5,"column":61},"action":"insert","lines":["ServiceInterface"],"id":30}],[{"start":{"row":5,"column":61},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":6,"column":0},"end":{"row":6,"column":8},"action":"insert","lines":["        "]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["r"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["e"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["t"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["u"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["r"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":[" "],"id":32}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":31},"action":"insert","lines":["ServiceInterface"],"id":33}],[{"start":{"row":6,"column":31},"end":{"row":6,"column":33},"action":"insert","lines":["()"],"id":34}],[{"start":{"row":6,"column":33},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":7,"column":0},"end":{"row":7,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"remove","lines":["    "],"id":36},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":37}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":38}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["d"],"id":39},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["f"],"id":40}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["e"],"id":41},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":[" "],"id":42}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["g"],"id":43},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["e"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["t"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["_"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["u"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["e"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["r"],"id":44},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["e"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["u"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["X"],"id":45},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["X"]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["X"],"id":46},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["X"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["a"],"id":47},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["c"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["c"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["e"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["s"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["s"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["t"],"id":48},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["o"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["k"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["e"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":26},"action":"insert","lines":["()"],"id":49}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["s"],"id":50},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["e"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["l"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["k"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["f"]}],[{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"remove","lines":["f"],"id":51},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"remove","lines":["k"]}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["f"],"id":52},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":[","]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":[" "],"id":53},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["u"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["s"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["e"]},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["r"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["_"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["i"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["d"]}],[{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":[":"],"id":54}],[{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":[" "],"id":55},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["i"]},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["n"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":[":"],"id":56}],[{"start":{"row":8,"column":45},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["a"],"id":58},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["c"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["c"]}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":11},"action":"remove","lines":["acc"],"id":59},{"start":{"row":9,"column":8},"end":{"row":9,"column":24},"action":"insert","lines":["access_token_dto"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":[" "],"id":60},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["="]}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":[" "],"id":61},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["s"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["e"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["l"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["f"]}],[{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["."],"id":62},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["i"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["n"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["t"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["e"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["r"]},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["f"]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["a"]}],[{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["c"],"id":63},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"insert","lines":["."],"id":64}],[{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"insert","lines":["g"],"id":65},{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"insert","lines":["e"]},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":42},"end":{"row":9,"column":45},"action":"remove","lines":["get"],"id":66},{"start":{"row":9,"column":42},"end":{"row":9,"column":58},"action":"insert","lines":["get_access_token"]}],[{"start":{"row":9,"column":58},"end":{"row":9,"column":60},"action":"insert","lines":["()"],"id":67}],[{"start":{"row":9,"column":59},"end":{"row":9,"column":60},"action":"insert","lines":["u"],"id":68},{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"insert","lines":["s"]},{"start":{"row":9,"column":61},"end":{"row":9,"column":62},"action":"insert","lines":["e"]},{"start":{"row":9,"column":62},"end":{"row":9,"column":63},"action":"insert","lines":["r"]},{"start":{"row":9,"column":63},"end":{"row":9,"column":64},"action":"insert","lines":["_"]},{"start":{"row":9,"column":64},"end":{"row":9,"column":65},"action":"insert","lines":["i"]},{"start":{"row":9,"column":65},"end":{"row":9,"column":66},"action":"insert","lines":["d"]}],[{"start":{"row":9,"column":66},"end":{"row":9,"column":67},"action":"insert","lines":["="],"id":69},{"start":{"row":9,"column":67},"end":{"row":9,"column":68},"action":"insert","lines":["u"]},{"start":{"row":9,"column":68},"end":{"row":9,"column":69},"action":"insert","lines":["s"]},{"start":{"row":9,"column":69},"end":{"row":9,"column":70},"action":"insert","lines":["e"]},{"start":{"row":9,"column":70},"end":{"row":9,"column":71},"action":"insert","lines":["r"]}],[{"start":{"row":9,"column":67},"end":{"row":9,"column":71},"action":"remove","lines":["user"],"id":70},{"start":{"row":9,"column":67},"end":{"row":9,"column":74},"action":"insert","lines":["user_id"]}],[{"start":{"row":9,"column":75},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":71},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["r"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["e"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["t"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["u"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["r"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":[" "],"id":72},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["a"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["c"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["c"]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":18},"action":"remove","lines":["acc"],"id":73},{"start":{"row":10,"column":15},"end":{"row":10,"column":31},"action":"insert","lines":["access_token_dto"]}],[{"start":{"row":11,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["","","","class AuthService:","    @property","    def interface(self):","        from fb_post_auth.interfaces.service_interface import ServiceInterface","        return ServiceInterface()","","    def get_user_dtos(self, user_ids: List[int]):","        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)","","        # TODO: Convert to DTO in this app","        return user_dtos",""],"id":74},{"start":{"row":10,"column":31},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":75}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["_"],"id":76},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["d"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["t"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["o"]}]]},"timestamp":1594307495519}