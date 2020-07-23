{"filter":false,"title":"get_total_reaction_count_interactor.py","tooltip":"/fb_post_learning/fb_post_v2/interactors/get_total_reaction_count_interactor.py","undoManager":{"mark":81,"position":81,"stack":[[{"start":{"row":0,"column":0},"end":{"row":29,"column":23},"action":"insert","lines":["","from fb_post_v2.interactors.storages import StorageInterface","","from fb_post_v2.interactors.presenters import PresenterInterface","","","class GetRepliesForCommentInteractor:","","    def __init__(self, storage: StorageInterface,","                 presenter: PresenterInterface):","        self.storage = storage","        self.presenter = presenter","","    def get_replies_for_comment(self, comment_id: int):","        is_valid_comment_id = self.storage.is_valid_comment_id(","            comment_id = comment_id","        )","        invalid_comment_id_given = not is_valid_comment_id","","        if invalid_comment_id_given:","            self.presenter.raise_invalid_comment_id_exception()","            return","","        list_of_replies_dict = self.storage.get_replies_for_comment(","            comment_id = comment_id","        )","        response = self.presenter.get_replies_for_comment_response(","            list_of_replies_dict = list_of_replies_dict","        )","        return response"],"id":1}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":36},"action":"remove","lines":["GetRepliesForCommentInteractor"],"id":2},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["G"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["e"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["t"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["T"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["o"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["t"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["l"],"id":3},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["R"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["e"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["a"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["c"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["t"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["i"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["n"],"id":4},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["C"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["o"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["u"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["t"],"id":5},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["I"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["t"],"id":6},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["e"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["r"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["a"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["c"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["t"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["o"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["r"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":31},"action":"remove","lines":["replies_for_comment"],"id":7},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["t"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["o"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["a"]}],[{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"remove","lines":["a"],"id":8}],[{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["t"],"id":9},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["a"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["l"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["_"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["r"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["e"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["a"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["c"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["i"],"id":10},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["o"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["n"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["_"]}],[{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["c"],"id":11},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["o"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["u"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["n"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":53},"end":{"row":13,"column":54},"action":"remove","lines":["t"],"id":12},{"start":{"row":13,"column":52},"end":{"row":13,"column":53},"action":"remove","lines":["n"]},{"start":{"row":13,"column":51},"end":{"row":13,"column":52},"action":"remove","lines":["i"]},{"start":{"row":13,"column":50},"end":{"row":13,"column":51},"action":"remove","lines":[" "]},{"start":{"row":13,"column":49},"end":{"row":13,"column":50},"action":"remove","lines":[":"]},{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"remove","lines":["d"]},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"remove","lines":["i"]},{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"remove","lines":["_"]},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"remove","lines":["t"]},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"remove","lines":["n"]},{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"remove","lines":["e"]},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"remove","lines":["m"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"remove","lines":["m"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"remove","lines":["o"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"remove","lines":["c"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"remove","lines":[","],"id":13}],[{"start":{"row":13,"column":39},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":15},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":30,"column":0},"action":"remove","lines":["","        is_valid_comment_id = self.storage.is_valid_comment_id(","            comment_id = comment_id","        )","        invalid_comment_id_given = not is_valid_comment_id","","        if invalid_comment_id_given:","            self.presenter.raise_invalid_comment_id_exception()","            return","","        list_of_replies_dict = self.storage.get_replies_for_comment(","            comment_id = comment_id","        )","        response = self.presenter.get_replies_for_comment_response(","            list_of_replies_dict = list_of_replies_dict","        )",""],"id":16}],[{"start":{"row":13,"column":39},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["c"],"id":18},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["o"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["u"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["n"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["t"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["_"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["d"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["i"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["c"]}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["t"],"id":19}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":[" "],"id":20},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["="]}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":[" "],"id":21}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["s"],"id":22},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["e"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["l"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["f"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":["."]}],[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["p"],"id":23},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["r"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["e"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["s"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["n"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["t"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["e"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["r"]}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["r"],"id":24},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["e"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["t"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["n"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["e"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["s"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["e"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["r"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["s"],"id":25},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["t"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["o"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["r"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["a"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["g"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["e"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["."]}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["g"],"id":26},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["e"]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"insert","lines":["t"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"insert","lines":["_"]},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"insert","lines":["o"],"id":27},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"insert","lines":["a"]}],[{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"remove","lines":["a"],"id":28}],[{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"insert","lines":["t"],"id":29}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":41},"action":"remove","lines":["get_tot"],"id":30},{"start":{"row":14,"column":34},"end":{"row":14,"column":58},"action":"insert","lines":["get_total_reaction_count"]}],[{"start":{"row":14,"column":58},"end":{"row":14,"column":60},"action":"insert","lines":["()"],"id":31}],[{"start":{"row":14,"column":60},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":15,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["        "]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["r"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["p"],"id":33}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"remove","lines":["p"],"id":34},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"remove","lines":["s"]}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["e"],"id":35},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["s"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["p"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["o"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["n"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["s"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":[" "],"id":36}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["="],"id":37}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":[" "],"id":38},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["s"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["e"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["l"],"id":39},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["e"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"remove","lines":["s"]}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["s"],"id":40},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["l"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["e"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["."]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["f"]}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["f"],"id":41},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["."]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["e"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["l"]}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["e"],"id":42},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["l"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["f"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["."]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["p"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["e"],"id":43},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":28},"action":"remove","lines":["pres"],"id":44},{"start":{"row":15,"column":24},"end":{"row":15,"column":33},"action":"insert","lines":["presenter"]}],[{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["."],"id":45},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["g"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["e"]},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["_"],"id":46},{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":["t"]},{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":34},"end":{"row":15,"column":40},"action":"remove","lines":["get_to"],"id":47},{"start":{"row":15,"column":34},"end":{"row":15,"column":69},"action":"insert","lines":["get_total_reaction_count_response()"]}],[{"start":{"row":15,"column":68},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":16,"column":0},"end":{"row":16,"column":12},"action":"insert","lines":["            "]},{"start":{"row":16,"column":12},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["c"],"id":49},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["o"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["u"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["t"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"remove","lines":["n"],"id":50},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"remove","lines":["t"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"remove","lines":["u"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"remove","lines":["o"]}],[{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["c"],"id":51},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"remove","lines":["o"],"id":52},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"remove","lines":["c"]},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"remove","lines":["c"]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["o"],"id":53},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["u"]}],[{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"remove","lines":["u"],"id":54},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"remove","lines":["o"]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["c"],"id":55},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["o"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["u"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":16},"action":"remove","lines":["coun"],"id":56},{"start":{"row":16,"column":12},"end":{"row":16,"column":22},"action":"insert","lines":["count_dict"]}],[{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"insert","lines":["="],"id":57},{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"insert","lines":["c"]},{"start":{"row":16,"column":24},"end":{"row":16,"column":25},"action":"insert","lines":["o"]},{"start":{"row":16,"column":25},"end":{"row":16,"column":26},"action":"insert","lines":["u"]}],[{"start":{"row":16,"column":23},"end":{"row":16,"column":26},"action":"remove","lines":["cou"],"id":58},{"start":{"row":16,"column":23},"end":{"row":16,"column":33},"action":"insert","lines":["count_dict"]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":12},"action":"remove","lines":["    "],"id":59}],[{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"remove","lines":["e"],"id":60},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"remove","lines":["s"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"remove","lines":["n"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"remove","lines":["o"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"remove","lines":["p"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"remove","lines":["s"]},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"remove","lines":["e"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"remove","lines":["r"]}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["c"],"id":61},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["o"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["u"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["n"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":20},"action":"remove","lines":["count"],"id":62},{"start":{"row":18,"column":15},"end":{"row":18,"column":25},"action":"insert","lines":["count_dict"]}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"remove","lines":["t"],"id":63},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"remove","lines":["c"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"remove","lines":["i"]},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"remove","lines":["d"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"remove","lines":["_"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"remove","lines":["t"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"remove","lines":["n"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"remove","lines":["u"]},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"remove","lines":["o"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"remove","lines":["c"]}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["r"],"id":64},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["e"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":18},"action":"remove","lines":["res"],"id":65},{"start":{"row":18,"column":15},"end":{"row":18,"column":23},"action":"insert","lines":["response"]}],[{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"insert","lines":["_"],"id":66},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"insert","lines":["d"]},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"insert","lines":["t"]},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"insert","lines":["o"]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":22},"action":"remove","lines":["count_dict"],"id":67},{"start":{"row":16,"column":12},"end":{"row":16,"column":40},"action":"insert","lines":["get_total_reaction_count_dto"]}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["_"],"id":68},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["t"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["o"],"id":69},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["t"]}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["d"],"id":70},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["t"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["o"]}],[{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":["_"],"id":71},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":["d"]},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":["t"]},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":["o"]}],[{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"remove","lines":["o"],"id":72},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"remove","lines":["t"]},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"remove","lines":["d"]},{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"remove","lines":["_"]}],[{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":["_"],"id":78},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":["d"]},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":["t"]},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["R"],"id":79},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["e"]},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["a"]},{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["c"]},{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["t"]},{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":["i"]},{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":["o"]},{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["r"],"id":80},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["e"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["a"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["c"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["t"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["i"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["o"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["n"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["R"],"id":81},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["e"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["a"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["c"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["c"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["t"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["i"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["o"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["r"],"id":82},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["e"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["a"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["c"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["t"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["i"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["o"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["n"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["_"]}],[{"start":{"row":10,"column":32},"end":{"row":10,"column":33},"action":"insert","lines":["r"],"id":83},{"start":{"row":10,"column":33},"end":{"row":10,"column":34},"action":"insert","lines":["e"]},{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"insert","lines":["a"]},{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["a"]},{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"insert","lines":["c"]},{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"insert","lines":["t"]},{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"insert","lines":["i"]},{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"insert","lines":["o"]},{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"insert","lines":["n"]},{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"insert","lines":["_"]}],[{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["r"],"id":84},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["e"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["a"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["c"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["t"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["i"]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"insert","lines":["o"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["_"],"id":85}],[{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"remove","lines":["c"],"id":86}],[{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"remove","lines":["a"],"id":87}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":44},"end":{"row":1,"column":44},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590059055857,"hash":"21f65243624a50bfbb39b830ed371006d3b70405"}