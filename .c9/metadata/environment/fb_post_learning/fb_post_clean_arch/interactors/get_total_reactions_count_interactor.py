{"filter":false,"title":"get_total_reactions_count_interactor.py","tooltip":"/fb_post_learning/fb_post_clean_arch/interactors/get_total_reactions_count_interactor.py","undoManager":{"mark":90,"position":90,"stack":[[{"start":{"row":0,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId","from fb_post_clean_arch.interactors.presenters.presenter_interface import \\","    PresenterInterface","from fb_post_clean_arch.interactors.storages.storage_interface import \\","    StorageInterface","","","class CreateCommentInteractor:","","    def __init__(self, storage: StorageInterface):","        self.storage = storage","","    def create_comment(self, post_id: int,","                       comment_text: str,","                       user_id: int,","                       presenter: PresenterInterface):","        try:","            self.storage.validate_post_id(post_id=post_id)","        except InvalidPostId:","            presenter.raise_exception_for_invalid_post()","            return","","        comment_id = self.storage.create_comment(","            post_id=post_id,","            comment_text=comment_text,","            user_id=user_id)","","        return presenter.get_create_comment_response(","            comment_id=comment_id)",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId",""],"id":2}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":29},"action":"remove","lines":["CreateCommentInteractor"],"id":3},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["G"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["e"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["T"],"id":4},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["o"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["t"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["a"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["l"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["R"]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["e"],"id":5},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["a"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["c"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["t"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["i"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["o"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["s"],"id":6},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["C"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["o"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["u"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["n"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["I"],"id":7},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["n"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["t"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["e"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["a"],"id":8},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["c"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["t"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["o"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["r"],"id":9}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["r"],"id":10}],[{"start":{"row":6,"column":39},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":14}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["d"],"id":15},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["e"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":[" "],"id":16},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["_"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["_"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["i"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["n"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["i"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["t"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["_"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":18},"action":"insert","lines":["()"],"id":17}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":[";"],"id":18}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":[";"],"id":19}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":[":"],"id":20}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["s"],"id":21},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["e"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["l"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["f"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":[","]}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":[" "],"id":22},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["s"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["t"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["r"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["o"],"id":23},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["r"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["o"],"id":24},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["r"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["a"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["g"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["e"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":[":"]}],[{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":[" "],"id":25},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["s"],"id":26}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["S"],"id":27},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["t"]},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":35},"action":"remove","lines":["Sto"],"id":28},{"start":{"row":8,"column":32},"end":{"row":8,"column":48},"action":"insert","lines":["StorageInterface"]}],[{"start":{"row":8,"column":50},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["s"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["e"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["l"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["f"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["."]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["s"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["t"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":16},"action":"remove","lines":["sto"],"id":30},{"start":{"row":9,"column":13},"end":{"row":9,"column":20},"action":"insert","lines":["storage"]}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":[" "],"id":31},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["="]}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":[" "],"id":32},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["t"],"id":33},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["o"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["r"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["a"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["g"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["e"],"id":34}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":35}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "],"id":36}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["d"],"id":37},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["e"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["g"],"id":39},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["e"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["t"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["_"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["o"],"id":40},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["t"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["a"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["l"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["_"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["c"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["u"],"id":41},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["n"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["t"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["_"]}],[{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"remove","lines":["_"],"id":42},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"remove","lines":["t"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":["n"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"remove","lines":["u"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"remove","lines":["o"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"remove","lines":["c"]}],[{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["r"],"id":43},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["e"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["a"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["c"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["t"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["i"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":["o"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["n"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["_"],"id":44},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["c"]},{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":["o"]},{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":["u"]},{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"insert","lines":["n"]},{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["_"],"id":45}],[{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"remove","lines":["_"],"id":46}],[{"start":{"row":11,"column":33},"end":{"row":11,"column":35},"action":"insert","lines":["()"],"id":47}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":[":"],"id":48}],[{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"insert","lines":["s"],"id":49},{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":["e"]},{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"insert","lines":["l"]},{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"insert","lines":["f"]}],[{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"insert","lines":[","],"id":50}],[{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"insert","lines":[" "],"id":51}],[{"start":{"row":12,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["    def __init__(self, storage: StorageInterface):","        self.storage = storage",""],"id":52}],[{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["s"],"id":53},{"start":{"row":11,"column":41},"end":{"row":11,"column":42},"action":"insert","lines":["t"]},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"insert","lines":["o"]},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"insert","lines":["r"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["a"]},{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"insert","lines":["g"]},{"start":{"row":11,"column":46},"end":{"row":11,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":47},"end":{"row":11,"column":48},"action":"insert","lines":[" "],"id":54},{"start":{"row":11,"column":48},"end":{"row":11,"column":49},"action":"insert","lines":["="]}],[{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"insert","lines":[" "],"id":55},{"start":{"row":11,"column":50},"end":{"row":11,"column":51},"action":"insert","lines":["="]}],[{"start":{"row":11,"column":50},"end":{"row":11,"column":51},"action":"remove","lines":["="],"id":56}],[{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"remove","lines":[" "],"id":57},{"start":{"row":11,"column":48},"end":{"row":11,"column":49},"action":"remove","lines":["="]},{"start":{"row":11,"column":47},"end":{"row":11,"column":48},"action":"remove","lines":[" "]},{"start":{"row":11,"column":46},"end":{"row":11,"column":47},"action":"remove","lines":["e"]},{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"remove","lines":["g"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"remove","lines":["a"]},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"remove","lines":["r"]},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"remove","lines":["o"]},{"start":{"row":11,"column":41},"end":{"row":11,"column":42},"action":"remove","lines":["t"]},{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"remove","lines":["s"]}],[{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["p"],"id":58},{"start":{"row":11,"column":41},"end":{"row":11,"column":42},"action":"insert","lines":["r"]},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"insert","lines":["e"]},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"insert","lines":["s"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["e"]},{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"insert","lines":["n"]},{"start":{"row":11,"column":46},"end":{"row":11,"column":47},"action":"insert","lines":["t"]},{"start":{"row":11,"column":47},"end":{"row":11,"column":48},"action":"insert","lines":["e"]},{"start":{"row":11,"column":48},"end":{"row":11,"column":49},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"insert","lines":[" "],"id":59}],[{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"remove","lines":[" "],"id":60}],[{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"insert","lines":["="],"id":61},{"start":{"row":11,"column":50},"end":{"row":11,"column":51},"action":"insert","lines":["P"]}],[{"start":{"row":11,"column":50},"end":{"row":11,"column":51},"action":"remove","lines":["P"],"id":62},{"start":{"row":11,"column":50},"end":{"row":11,"column":68},"action":"insert","lines":["PresenterInterface"]}],[{"start":{"row":11,"column":70},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":12,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["s"],"id":64},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["e"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["l"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["f"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["."]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["s"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["t"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["r"],"id":65},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["a"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["g"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["e"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["."]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["c"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["e"],"id":66},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["a"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["t"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["e"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["_"]},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":["c"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"insert","lines":["o"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":["m"]},{"start":{"row":12,"column":31},"end":{"row":12,"column":32},"action":"insert","lines":["m"]}],[{"start":{"row":12,"column":32},"end":{"row":12,"column":33},"action":"insert","lines":["e"],"id":67},{"start":{"row":12,"column":33},"end":{"row":12,"column":34},"action":"insert","lines":["n"]},{"start":{"row":12,"column":34},"end":{"row":12,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":34},"end":{"row":12,"column":35},"action":"remove","lines":["t"],"id":68},{"start":{"row":12,"column":33},"end":{"row":12,"column":34},"action":"remove","lines":["n"]},{"start":{"row":12,"column":32},"end":{"row":12,"column":33},"action":"remove","lines":["e"]},{"start":{"row":12,"column":31},"end":{"row":12,"column":32},"action":"remove","lines":["m"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"remove","lines":["m"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"remove","lines":["o"]},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"remove","lines":["c"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"remove","lines":["_"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"remove","lines":["e"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"remove","lines":["t"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":["a"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["e"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":["r"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["c"]}],[{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["g"],"id":69},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["e"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["t"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["_"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["t"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["o"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":21},"end":{"row":12,"column":28},"action":"remove","lines":["get_tot"],"id":70},{"start":{"row":12,"column":21},"end":{"row":12,"column":46},"action":"insert","lines":["get_total_reactions_count"]}],[{"start":{"row":12,"column":46},"end":{"row":12,"column":48},"action":"insert","lines":["()"],"id":71}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["r"],"id":72},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["e"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["a"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["c"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["t"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["i"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["o"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["n"]},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["_"],"id":73},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["c"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["o"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["u"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["n"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["t"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["="]}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":[" "],"id":74}],[{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":[" "],"id":75}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["_"],"id":76},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["d"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["i"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["c"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":71},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"insert","lines":["        "]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["r"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["t"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["u"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["r"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":[" "],"id":78}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["p"],"id":79},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["r"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["e"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["s"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["e"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["n"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["t"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["e"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["r"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["."]}],[{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["g"],"id":80},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["e"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["_"],"id":81},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["r"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"remove","lines":["e"],"id":82},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["r"]}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["t"],"id":83},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["o"]}],[{"start":{"row":13,"column":25},"end":{"row":13,"column":31},"action":"remove","lines":["get_to"],"id":84},{"start":{"row":13,"column":25},"end":{"row":13,"column":50},"action":"insert","lines":["get_total_reactions_count"]}],[{"start":{"row":13,"column":50},"end":{"row":13,"column":51},"action":"insert","lines":["_"],"id":85},{"start":{"row":13,"column":51},"end":{"row":13,"column":52},"action":"insert","lines":["r"]},{"start":{"row":13,"column":52},"end":{"row":13,"column":53},"action":"insert","lines":["e"]},{"start":{"row":13,"column":53},"end":{"row":13,"column":54},"action":"insert","lines":["s"]},{"start":{"row":13,"column":54},"end":{"row":13,"column":55},"action":"insert","lines":["p"]},{"start":{"row":13,"column":55},"end":{"row":13,"column":56},"action":"insert","lines":["o"]},{"start":{"row":13,"column":56},"end":{"row":13,"column":57},"action":"insert","lines":["n"]},{"start":{"row":13,"column":57},"end":{"row":13,"column":58},"action":"insert","lines":["s"]},{"start":{"row":13,"column":58},"end":{"row":13,"column":59},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":59},"end":{"row":13,"column":61},"action":"insert","lines":["()"],"id":86}],[{"start":{"row":13,"column":60},"end":{"row":13,"column":61},"action":"insert","lines":["r"],"id":87},{"start":{"row":13,"column":61},"end":{"row":13,"column":62},"action":"insert","lines":["e"]},{"start":{"row":13,"column":62},"end":{"row":13,"column":63},"action":"insert","lines":["a"]},{"start":{"row":13,"column":63},"end":{"row":13,"column":64},"action":"insert","lines":["c"]},{"start":{"row":13,"column":64},"end":{"row":13,"column":65},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":60},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":88},{"start":{"row":14,"column":0},"end":{"row":14,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":17},"action":"remove","lines":["react"],"id":89},{"start":{"row":14,"column":12},"end":{"row":14,"column":32},"action":"insert","lines":["reactions_count_dict"]}],[{"start":{"row":14,"column":32},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":90},{"start":{"row":15,"column":0},"end":{"row":15,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":16,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["","    def create_comment(self, post_id: int,","                       comment_text: str,","                       user_id: int,","                       presenter: PresenterInterface):","        try:","            self.storage.validate_post_id(post_id=post_id)","        except InvalidPostId:","            presenter.raise_exception_for_invalid_post()","            return","","        comment_id = self.storage.create_comment(","            post_id=post_id,","            comment_text=comment_text,","            user_id=user_id)","","        return presenter.get_create_comment_response(","            comment_id=comment_id)",""],"id":91}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":0},"end":{"row":10,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589607679529,"hash":"4cb2c3dcc084f6f9814e44ab60914b0d8d59109a"}