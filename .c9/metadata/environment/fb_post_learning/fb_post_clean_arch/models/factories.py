{"filter":false,"title":"factories.py","tooltip":"/fb_post_learning/fb_post_clean_arch/models/factories.py","undoManager":{"mark":43,"position":43,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":2},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"insert","lines":["# "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["# "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":2},"action":"insert","lines":["# "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["# "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["# "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"insert","lines":["# "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["# "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["# "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":9,"column":0},"end":{"row":23,"column":0},"action":"remove","lines":["# class UserFactory(factory.django.DjangoModelFactory):","#     class Meta:","#         model = User","#     name = factory.Sequence(lambda n: \"user%d\" % n)","#     profile_pic = factory.Sequence(lambda n: \"profile_pic/user%d.png\" % n)","","","# class PostFactory(factory.django.DjangoModelFactory):","#     class Meta:","#         model = Post","","#     posted_by = factory.SubFactory(UserFactory)","#     content = factory.Sequence(lambda n: \"post content%d\" % n)","#     posted_at = factory.LazyFunction(datetime.datetime.now)",""],"id":3},{"start":{"row":9,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["import factory","","class UserFactory(factory.django.DjangoModelFactory):","    class Meta:","        model = User","    name = factory.Sequence(lambda n: \"user%d\" % n)","    profile_pic = factory.Sequence(lambda n: \"profile_pic/user%d.png\" % n)","","","class PostFactory(factory.django.DjangoModelFactory):","    class Meta:","        model = Post","    user = factory.SubFactory(UserFactory)","    post_content = factory.Sequence(lambda n: \"post content%d\" % n)","    pub_date_time = factory.LazyFunction(datetime.datetime.now)",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":5},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":6},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["f"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["a"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["c"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["t"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["o"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["r"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["y"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"],"id":7},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["p"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["o"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["r"],"id":8}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"],"id":9}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":10},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["d"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["a"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["t"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":11},"action":"remove","lines":["date"],"id":11},{"start":{"row":1,"column":7},"end":{"row":1,"column":15},"action":"insert","lines":["datetime"]}],[{"start":{"row":1,"column":15},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["i"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["m"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["p"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["o"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["r"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":[" "],"id":13},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["f"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["a"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["c"]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["t"],"id":14},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["o"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["r"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["y"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["."]}],[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["."],"id":15},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["y"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["r"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["o"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["t"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["c"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["a"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["f"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":[" "]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":[" "],"id":16},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["f"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["b"]}],[{"start":{"row":2,"column":7},"end":{"row":2,"column":9},"action":"remove","lines":["fb"],"id":17},{"start":{"row":2,"column":7},"end":{"row":2,"column":25},"action":"insert","lines":["fb_post_clean_arch"]}],[{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["."],"id":18},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["m"]},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["o"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["d"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["l"]}],[{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"remove","lines":["l"],"id":19}],[{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["e"],"id":20},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["l"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":[" "],"id":21},{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"insert","lines":["i"]},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"insert","lines":["m"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["p"]},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":["o"]},{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["r"]},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":[" "],"id":22},{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"insert","lines":["*"]},{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"insert","lines":["*"]}],[{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"remove","lines":["*"],"id":23}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":24}],[{"start":{"row":1,"column":15},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":25}],[{"start":{"row":1,"column":15},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":26}],[{"start":{"row":3,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["","# import datetime","","# from fb_post.models import (","#     User, Post, Comment, Reaction, REACTION_CHOICES","# )","# import factory","# import factory.fuzzy",""],"id":27},{"start":{"row":2,"column":41},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":15},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":28}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["import factory","import datetime","",""],"id":29}],[{"start":{"row":1,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["import factory","import datetime","",""],"id":30}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":31}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["t"],"id":32},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"remove","lines":["r"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["o"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["p"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["m"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["i"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":33},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":9,"column":51},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["u"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["s"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["e"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["r"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["a"],"id":35},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["m"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":[" "],"id":36},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":[" "],"id":37},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["f"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["a"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["c"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["t"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["o"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["r"]}],[{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["y"],"id":38},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["."]},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"remove","lines":["s"],"id":39}],[{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["S"],"id":40},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":23},"end":{"row":10,"column":25},"action":"remove","lines":["Se"],"id":41},{"start":{"row":10,"column":23},"end":{"row":10,"column":31},"action":"insert","lines":["Sequence"]}],[{"start":{"row":10,"column":31},"end":{"row":10,"column":33},"action":"insert","lines":["()"],"id":42}],[{"start":{"row":10,"column":32},"end":{"row":10,"column":54},"action":"insert","lines":["lambda n: \"user%d\" % n"],"id":43}],[{"start":{"row":10,"column":47},"end":{"row":10,"column":48},"action":"insert","lines":["n"],"id":44},{"start":{"row":10,"column":48},"end":{"row":10,"column":49},"action":"insert","lines":["a"]},{"start":{"row":10,"column":49},"end":{"row":10,"column":50},"action":"insert","lines":["m"]},{"start":{"row":10,"column":50},"end":{"row":10,"column":51},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":51},"end":{"row":10,"column":52},"action":"insert","lines":[" "],"id":45}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":42},"end":{"row":17,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1592927617517,"hash":"127265b5b7c0e3c59b9c1f497458637661e45ad4"}