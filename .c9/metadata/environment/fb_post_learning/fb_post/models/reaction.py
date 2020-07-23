{"filter":false,"title":"reaction.py","tooltip":"/fb_post_learning/fb_post/models/reaction.py","undoManager":{"mark":91,"position":91,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["from django.db import models",""],"id":1}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["class Reaction(models.Model):","    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)","    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)","    reaction=models.CharField(max_length=100,choices=REACTION_CHOICES)","    reacted_by=models.ForeignKey(User,on_delete=models.CASCADE)","    reacted_at=models.DateTimeField(auto_now=True)",""],"id":3}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":4},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":5},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["f"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["b"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["_"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["p"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":9},"action":"remove","lines":["fb_p"],"id":6},{"start":{"row":2,"column":5},"end":{"row":2,"column":12},"action":"insert","lines":["fb_post"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["."],"id":7},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["m"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["o"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["d"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["e"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["l"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":[" "],"id":8}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"remove","lines":[" "],"id":9}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["."],"id":10},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["u"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["s"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["e"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":[" "],"id":11},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["i"]},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["p"]},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"remove","lines":["o"],"id":12},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"remove","lines":["p"]}],[{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["m"],"id":13},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["p"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["o"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["r"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":[" "],"id":14},{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":["U"]},{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"insert","lines":["s"]},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"insert","lines":["e"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":36},"end":{"row":3,"column":0},"action":"insert","lines":["c",""],"id":15}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"],"id":16},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":17},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"remove","lines":["c"],"id":18}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["b"],"id":19}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":7},"action":"remove","lines":["fb"],"id":20},{"start":{"row":3,"column":5},"end":{"row":3,"column":12},"action":"insert","lines":["fb_post"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["."],"id":21},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["m"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["o"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["d"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["e"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["l"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["."],"id":22},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["P"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["o"],"id":23},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["P"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["p"],"id":24},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["o"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["s"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":[" "],"id":25},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["i"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["m"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["p"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["o"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["r"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":[" "],"id":26},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["P"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["o"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["s"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":36},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["f"]},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["r"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["o"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":[" "],"id":28},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["from f",""],"id":29},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["from fb_post.models.post import Post",""]}],[{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"remove","lines":["t"],"id":30}],[{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"remove","lines":["t"],"id":31},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"remove","lines":["s"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"remove","lines":["o"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["c"],"id":32},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["o"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["m"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["m"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["e"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["n"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"remove","lines":["s"],"id":33},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"remove","lines":["o"]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"remove","lines":["P"]}],[{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["C"],"id":34},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["o"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["m"]},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"insert","lines":["m"]},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"insert","lines":["e"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["n"]},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":42},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["F"],"id":36},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["R"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["O"]}],[{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"remove","lines":["O"],"id":37},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"remove","lines":["R"]},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["F"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["f"],"id":38},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["r"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["o"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":[" "],"id":39},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["f"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["b"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["o"],"id":40},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["b"]}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["f"],"id":41},{"start":{"row":6,"column":5},"end":{"row":6,"column":12},"action":"insert","lines":["fb_post"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["."],"id":42},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["C"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["O"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["N"]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["N"],"id":43},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["O"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["C"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["c"],"id":44},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["o"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["n"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["s"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["a"],"id":45},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["n"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["t"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["s"],"id":46},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["t"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["n"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["a"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["t"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["s"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["n"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["o"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["c"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["c"],"id":47},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["o"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["n"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["s"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["t"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["a"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["n"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["t"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["."],"id":48},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["e"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["n"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["u"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["_"],"id":49},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["c"]},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["o"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["n"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["s"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["t"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["a"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["n"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["t"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":[" "],"id":50},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["i"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["m"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["p"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["o"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":["r"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":[" "],"id":51},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"insert","lines":["R"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"insert","lines":["e"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":45},"end":{"row":6,"column":48},"action":"remove","lines":["Rea"],"id":52},{"start":{"row":6,"column":45},"end":{"row":6,"column":66},"action":"insert","lines":["ReactionTypeChoices()"]}],[{"start":{"row":6,"column":64},"end":{"row":6,"column":66},"action":"remove","lines":["()"],"id":53}],[{"start":{"row":6,"column":64},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":12,"column":30},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":[" "],"id":56}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":[" "],"id":57}],[{"start":{"row":13,"column":23},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["["],"id":59},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["]"]}],[{"start":{"row":14,"column":17},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":15,"column":0},"end":{"row":15,"column":12},"action":"insert","lines":["            "]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["\\"]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["\\"],"id":61}],[{"start":{"row":15,"column":12},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":62},{"start":{"row":16,"column":0},"end":{"row":16,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":14},"action":"insert","lines":["()"],"id":63}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["r"],"id":64},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["e"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["a"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["c"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["t"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["i"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["o"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["n"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["_"]}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["t"],"id":65},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["y"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["p"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["e"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["."]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["v"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["a"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["l"],"id":66},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["a"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["v"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["v"],"id":67},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["a"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["l"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["u"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":[")"],"id":68},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["e"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["u"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["l"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["a"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["v"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["."]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["e"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"remove","lines":["p"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["y"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["t"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["_"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["n"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"remove","lines":["o"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["i"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["t"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["c"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["a"],"id":69},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["e"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["r"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["("]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":14},"action":"insert","lines":["()"],"id":70}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["r"],"id":71},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["e"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["a"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["c"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["t"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["i"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["o"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["_"],"id":72},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["t"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["y"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["p"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["e"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["."]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["v"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["a"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["u"],"id":73},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["e"],"id":74},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["u"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["l"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["a"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["v"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["n"],"id":75},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["a"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["m"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":[","],"id":76}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":[" "],"id":77},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["r"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["e"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["a"]}],[{"start":{"row":15,"column":33},"end":{"row":15,"column":36},"action":"remove","lines":["rea"],"id":78},{"start":{"row":15,"column":33},"end":{"row":15,"column":46},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["."],"id":79},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["v"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["a"]},{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":["l"]},{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["u"]},{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":[" "],"id":80},{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":["f"]},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["o"]},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":[" "],"id":81}],[{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["r"],"id":82},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["e"]},{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["a"]},{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["c"]}],[{"start":{"row":15,"column":58},"end":{"row":15,"column":62},"action":"remove","lines":["reac"],"id":83},{"start":{"row":15,"column":58},"end":{"row":15,"column":71},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":15,"column":71},"end":{"row":15,"column":72},"action":"insert","lines":[" "],"id":84},{"start":{"row":15,"column":72},"end":{"row":15,"column":73},"action":"insert","lines":["i"]},{"start":{"row":15,"column":73},"end":{"row":15,"column":74},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":74},"end":{"row":15,"column":75},"action":"insert","lines":[" "],"id":85}],[{"start":{"row":15,"column":75},"end":{"row":15,"column":94},"action":"insert","lines":["ReactionTypeChoices"],"id":86}],[{"start":{"row":16,"column":29},"end":{"row":16,"column":30},"action":"remove","lines":[")"],"id":87},{"start":{"row":16,"column":28},"end":{"row":16,"column":29},"action":"remove","lines":["S"]},{"start":{"row":16,"column":27},"end":{"row":16,"column":28},"action":"remove","lines":["E"]},{"start":{"row":16,"column":26},"end":{"row":16,"column":27},"action":"remove","lines":["C"]},{"start":{"row":16,"column":25},"end":{"row":16,"column":26},"action":"remove","lines":["I"]},{"start":{"row":16,"column":24},"end":{"row":16,"column":25},"action":"remove","lines":["O"]},{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"remove","lines":["H"]},{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"remove","lines":["C"]},{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"remove","lines":["_"]},{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"remove","lines":["N"]},{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"remove","lines":["O"]},{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"remove","lines":["I"]},{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"remove","lines":["T"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"remove","lines":["C"]}],[{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"remove","lines":["A"],"id":88},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"remove","lines":["E"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"remove","lines":["R"]}],[{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":[")"],"id":89}],[{"start":{"row":16,"column":13},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":90},{"start":{"row":17,"column":0},"end":{"row":17,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":12},"action":"remove","lines":["    "],"id":91},{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"remove","lines":[" "],"id":92},{"start":{"row":15,"column":53},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":12},"action":"insert","lines":["            "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":64},"end":{"row":6,"column":64},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":35,"mode":"ace/mode/python"}},"timestamp":1588852969558,"hash":"f4cdeb64bce262d30ebecaa67baa8747252e7bc2"}