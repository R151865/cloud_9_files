{"filter":false,"title":"get_post_reacted_by_user.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/utils/get_post_reacted_by_user.py","undoManager":{"mark":44,"position":44,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":1},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["# 11","def get_posts_reacted_by_user(user_id):","","    is_user_id_valid(user_id)","","    return list(Post.objects.filter(posted_by_id=user_id)\\","                    .values_list('id', flat=True)","               )","","","def get_user_with_reaction_in_dict(react):","    return {","        'user_id':react.reacted_by.id,","        'name':react.reacted_by.name,","        'profile_pic':react.reacted_by.profile_pic,","        'reaction':react.reaction","        }","",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":3},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":4}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["."],"id":5},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["u"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["t"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["i"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":10},"action":"remove","lines":["util"],"id":6},{"start":{"row":0,"column":6},"end":{"row":0,"column":18},"action":"insert","lines":["utils_checks"]}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":[" "],"id":7},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["i"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["m"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["p"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["o"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["r"]},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":[" "],"id":8},{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"insert","lines":["i"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":26},"end":{"row":0,"column":28},"action":"remove","lines":["is"],"id":9},{"start":{"row":0,"column":26},"end":{"row":0,"column":42},"action":"insert","lines":["is_user_id_valid"]}],[{"start":{"row":0,"column":42},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":12},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":13},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["f"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":7},"action":"remove","lines":["fb"],"id":14},{"start":{"row":0,"column":5},"end":{"row":0,"column":12},"action":"insert","lines":["fb_post"]}],[{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["."],"id":15},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["m"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":13},"end":{"row":0,"column":15},"action":"remove","lines":["mo"],"id":16},{"start":{"row":0,"column":13},"end":{"row":0,"column":19},"action":"insert","lines":["models"]}],[{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":[" "],"id":17},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["i"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["m"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["p"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["o"]},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"remove","lines":[" "],"id":19}],[{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":["t"],"id":20}],[{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"insert","lines":[" "],"id":21},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["R"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["R"],"id":22}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["p"],"id":23},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"remove","lines":["o"],"id":24},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["p"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["P"],"id":25},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["o"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["s"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":26},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":27},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["f"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["b"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["_"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["p"]}],[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["o"],"id":28},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["s"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["t"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["s"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["."]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["u"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["t"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["i"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["l"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":[" "],"id":29},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["i"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["m"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["p"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["o"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["r"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":[" "],"id":30},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["g"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["e"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["t"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["_"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["p"]},{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"insert","lines":["s"],"id":31},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"insert","lines":["t"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":["_"],"id":32}],[{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["r"],"id":33},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["e"]},{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":["a"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":40},"action":"remove","lines":["get_posts_rea"],"id":34},{"start":{"row":2,"column":27},"end":{"row":2,"column":52},"action":"insert","lines":["get_posts_reacted_by_user"]}],[{"start":{"row":2,"column":52},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":35}],[{"start":{"row":10,"column":28},"end":{"row":10,"column":29},"action":"insert","lines":["\\"],"id":36}],[{"start":{"row":10,"column":29},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"insert","lines":["    "],"id":38}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":12},"action":"insert","lines":["    "],"id":39}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":16},"action":"insert","lines":["    "],"id":40}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":20},"action":"insert","lines":["    "],"id":41}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":20},"action":"remove","lines":["    "],"id":42},{"start":{"row":12,"column":12},"end":{"row":12,"column":16},"action":"remove","lines":["    "]},{"start":{"row":12,"column":8},"end":{"row":12,"column":12},"action":"remove","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":50},"end":{"row":12,"column":0},"action":"remove","lines":["",""]},{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"remove","lines":["\\"]}],[{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"insert","lines":["\\"],"id":43}],[{"start":{"row":11,"column":50},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":12,"column":0},"end":{"row":12,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":22,"column":9},"end":{"row":23,"column":0},"action":"remove","lines":["",""],"id":45}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":22,"column":9},"end":{"row":22,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1587987636633,"hash":"769c8ee35ff34c9db4621ea8fdc8344a67f98a02"}