{"filter":false,"title":"auth_service.py","tooltip":"/git_practice/ib_miniprojects_backend/essentials_kit_management/adapters/auth_service.py","undoManager":{"mark":42,"position":42,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":31},"action":"insert","lines":["from typing import List","","","class AuthService:","    @property","    def interface(self):","        from auth_service.interfaces.token_interface import TokenInterface","        return TokenInterface()","","    def create_user_auth_tokens(self, user_id: int):","        access_token_dto = self.interface.create_user_auth_tokens(","            user_id=user_id","        )","        return access_token_dto"],"id":2}],[{"start":{"row":13,"column":31},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":4},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "],"id":6}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["d"],"id":7},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["e"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":[" "],"id":8},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["g"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["e"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["t"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["_"]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":12},"action":"remove","lines":["get_"],"id":9},{"start":{"row":15,"column":8},"end":{"row":15,"column":23},"action":"insert","lines":["get_user_dtos()"]}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["u"],"id":10},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["s"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"remove","lines":["e"],"id":11},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["s"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["u"]}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["s"],"id":12},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["e"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["l"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["f"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":[","]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":[" "],"id":13},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["u"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["s"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["e"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":32},"action":"remove","lines":["user"],"id":14},{"start":{"row":15,"column":28},"end":{"row":15,"column":35},"action":"insert","lines":["user_id"]}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["s"],"id":15},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":[":"]}],[{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":[" "],"id":16},{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":[":"]}],[{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"remove","lines":[":"],"id":17}],[{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":["L"],"id":18},{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"insert","lines":["i"]},{"start":{"row":15,"column":40},"end":{"row":15,"column":41},"action":"insert","lines":["s"]},{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":42},"end":{"row":15,"column":44},"action":"insert","lines":["[]"],"id":19}],[{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["i"],"id":20},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["n"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":[":"],"id":21}],[{"start":{"row":15,"column":49},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":16,"column":0},"end":{"row":16,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["u"],"id":23},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["s"]},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["e"]},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["r"]},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["_"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["d"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["t"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["o"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":[" "],"id":24},{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"insert","lines":[" "],"id":25},{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"insert","lines":["s"]},{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"insert","lines":["e"]},{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"insert","lines":["l"]},{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"insert","lines":["f"]}],[{"start":{"row":16,"column":24},"end":{"row":16,"column":25},"action":"insert","lines":["."],"id":26},{"start":{"row":16,"column":25},"end":{"row":16,"column":26},"action":"insert","lines":["i"]},{"start":{"row":16,"column":26},"end":{"row":16,"column":27},"action":"insert","lines":["n"]},{"start":{"row":16,"column":27},"end":{"row":16,"column":28},"action":"insert","lines":["t"]},{"start":{"row":16,"column":28},"end":{"row":16,"column":29},"action":"insert","lines":["e"]},{"start":{"row":16,"column":29},"end":{"row":16,"column":30},"action":"insert","lines":["r"]}],[{"start":{"row":16,"column":25},"end":{"row":16,"column":30},"action":"remove","lines":["inter"],"id":27},{"start":{"row":16,"column":25},"end":{"row":16,"column":36},"action":"insert","lines":["interface()"]}],[{"start":{"row":16,"column":34},"end":{"row":16,"column":36},"action":"remove","lines":["()"],"id":28}],[{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"insert","lines":["."],"id":29},{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["c"]}],[{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"remove","lines":["c"],"id":30}],[{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["g"],"id":31},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"insert","lines":["e"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":35},"end":{"row":16,"column":38},"action":"remove","lines":["get"],"id":32},{"start":{"row":16,"column":35},"end":{"row":16,"column":48},"action":"insert","lines":["get_user_dtos"]}],[{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"insert","lines":["9"],"id":33}],[{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"remove","lines":["9"],"id":34}],[{"start":{"row":16,"column":48},"end":{"row":16,"column":50},"action":"insert","lines":["()"],"id":35}],[{"start":{"row":16,"column":49},"end":{"row":16,"column":50},"action":"insert","lines":["u"],"id":36},{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"insert","lines":["s"]},{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":["e"]},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":["r"]},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":["_"]},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":["i"]},{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"insert","lines":["d"]},{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"insert","lines":["s"]}],[{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"insert","lines":["="],"id":37},{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"insert","lines":["u"]},{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"insert","lines":["s"]},{"start":{"row":16,"column":60},"end":{"row":16,"column":61},"action":"insert","lines":["e"]},{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"insert","lines":["r"]}],[{"start":{"row":16,"column":58},"end":{"row":16,"column":62},"action":"remove","lines":["user"],"id":38},{"start":{"row":16,"column":58},"end":{"row":16,"column":66},"action":"insert","lines":["user_ids"]}],[{"start":{"row":16,"column":67},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":17,"column":0},"end":{"row":17,"column":8},"action":"insert","lines":["        "]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["r"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["e"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["t"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["u"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["n"],"id":40}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":[" "],"id":41},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["a"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["c"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["c"]}],[{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"remove","lines":["c"],"id":42},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"remove","lines":["c"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"remove","lines":["a"]}],[{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["u"],"id":43},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["s"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["e"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":17,"column":15},"end":{"row":17,"column":19},"action":"remove","lines":["user"],"id":44},{"start":{"row":17,"column":15},"end":{"row":17,"column":24},"action":"insert","lines":["user_dtos"]}]]},"ace":{"folds":[],"scrolltop":23.5,"scrollleft":0,"selection":{"start":{"row":17,"column":24},"end":{"row":17,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1593706737571,"hash":"d72f2da56dc2cd73d540812bdc8abd796d5e383d"}