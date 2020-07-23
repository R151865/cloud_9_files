{"filter":false,"title":"get_user_posts.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/utils/get_user_posts.py","undoManager":{"mark":58,"position":58,"stack":[[{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["s"],"id":3},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["k"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["c"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["e"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":["h"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["c"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["v"],"id":4},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["a"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["l"]}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":15},"action":"remove","lines":["utils_val"],"id":5},{"start":{"row":3,"column":6},"end":{"row":3,"column":22},"action":"insert","lines":["utils_validators"]}],[{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["v"],"id":6},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["a"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["l"]}],[{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":["i"],"id":7},{"start":{"row":3,"column":37},"end":{"row":3,"column":38},"action":"insert","lines":["d"]},{"start":{"row":3,"column":38},"end":{"row":3,"column":39},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":43},"end":{"row":3,"column":52},"action":"remove","lines":["_id_valid"],"id":8}],[{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["v"],"id":9},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["a"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["l"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["l"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["i"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["d"],"id":10},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"remove","lines":["i"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"remove","lines":["l"]}],[{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["i"],"id":11},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["d"]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":12},"action":"remove","lines":["is_valid"],"id":12},{"start":{"row":24,"column":4},"end":{"row":24,"column":17},"action":"insert","lines":["is_valid_user"]}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":30},"action":"remove","lines":["user_id_valid"],"id":13}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["t"],"id":14},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["s"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["o"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["p"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["_"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["t"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["e"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["g"],"id":15},{"start":{"row":2,"column":6},"end":{"row":2,"column":27},"action":"insert","lines":["get_post_details_dict"]}],[{"start":{"row":8,"column":4},"end":{"row":17,"column":0},"action":"remove","lines":["comment_queryset = Comment.objects.select_related('commented_by')\\","                              .prefetch_related('reaction_set')","","    post_queryset = Post.objects\\","                        .select_related('posted_by')\\","                        .prefetch_related(","                            'reaction_set',","                            Prefetch('comment_set', queryset=comment_queryset)","                        ).filter(posted_by_id=user_id)#arrange properly",""],"id":16}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "],"id":17}],[{"start":{"row":16,"column":4},"end":{"row":25,"column":0},"action":"insert","lines":["comment_queryset = Comment.objects.select_related('commented_by')\\","                              .prefetch_related('reaction_set')","","    post_queryset = Post.objects\\","                        .select_related('posted_by')\\","                        .prefetch_related(","                            'reaction_set',","                            Prefetch('comment_set', queryset=comment_queryset)","                        ).filter(posted_by_id=user_id)#arrange properly",""],"id":18}],[{"start":{"row":15,"column":26},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":26,"column":0},"end":{"row":29,"column":0},"action":"remove","lines":["","    posts = get_posts_queryset(user_id)#not intent revealing","",""],"id":21}],[{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["t"],"id":22},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["e"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["s"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["y"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["r"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"remove","lines":["e"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["u"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"remove","lines":["q"]}],[{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["o"],"id":23},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["b"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["j"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":24},"action":"remove","lines":["    "],"id":24}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":24},"action":"remove","lines":["    "],"id":25}],[{"start":{"row":23,"column":24},"end":{"row":23,"column":28},"action":"remove","lines":["    "],"id":26}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":28},"action":"remove","lines":["    "],"id":27}],[{"start":{"row":25,"column":20},"end":{"row":25,"column":24},"action":"remove","lines":["    "],"id":28}],[{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"remove","lines":[")"],"id":29},{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"remove","lines":["s"]},{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"remove","lines":["t"]},{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"remove","lines":["s"]},{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"remove","lines":["o"]},{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"remove","lines":["p"]},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"remove","lines":["("]},{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"remove","lines":["n"]},{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"remove","lines":["e"]},{"start":{"row":26,"column":5},"end":{"row":26,"column":6},"action":"remove","lines":["l"]},{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"remove","lines":["#"]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":6,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["def get_posts_queryset(user_id):","","    ","    return post_queryset","",""],"id":30},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":[" "],"id":31}],[{"start":{"row":21,"column":23},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["f"],"id":33}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":["f"],"id":34}],[{"start":{"row":21,"column":23},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":35},"action":"insert","lines":["get_post_details_dict(post)"],"id":36}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":[" "],"id":37},{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["f"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["r"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["o"]}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"remove","lines":[" "],"id":39},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"remove","lines":["o"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"remove","lines":["r"]}],[{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["r"],"id":40}],[{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"remove","lines":["r"],"id":41}],[{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["o"],"id":42},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["r"]}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":[" "],"id":43},{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"insert","lines":["p"]},{"start":{"row":22,"column":41},"end":{"row":22,"column":42},"action":"insert","lines":["o"]},{"start":{"row":22,"column":42},"end":{"row":22,"column":43},"action":"insert","lines":["s"]},{"start":{"row":22,"column":43},"end":{"row":22,"column":44},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":44},"end":{"row":22,"column":45},"action":"insert","lines":["_"],"id":44},{"start":{"row":22,"column":45},"end":{"row":22,"column":46},"action":"insert","lines":["o"]},{"start":{"row":22,"column":46},"end":{"row":22,"column":47},"action":"insert","lines":["b"]}],[{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"insert","lines":[" "],"id":45},{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"insert","lines":["i"]}],[{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"remove","lines":["i"],"id":46},{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"remove","lines":[" "]}],[{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"insert","lines":["j"],"id":47}],[{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"insert","lines":[" "],"id":48},{"start":{"row":22,"column":49},"end":{"row":22,"column":50},"action":"insert","lines":["i"]},{"start":{"row":22,"column":50},"end":{"row":22,"column":51},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":51},"end":{"row":22,"column":52},"action":"insert","lines":[" "],"id":49},{"start":{"row":22,"column":52},"end":{"row":22,"column":53},"action":"insert","lines":["p"]},{"start":{"row":22,"column":53},"end":{"row":22,"column":54},"action":"insert","lines":["o"]},{"start":{"row":22,"column":54},"end":{"row":22,"column":55},"action":"insert","lines":["s"]},{"start":{"row":22,"column":55},"end":{"row":22,"column":56},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":56},"end":{"row":22,"column":57},"action":"insert","lines":["_"],"id":50},{"start":{"row":22,"column":57},"end":{"row":22,"column":58},"action":"insert","lines":["o"]},{"start":{"row":22,"column":58},"end":{"row":22,"column":59},"action":"insert","lines":["b"]},{"start":{"row":22,"column":59},"end":{"row":22,"column":60},"action":"insert","lines":["j"]}],[{"start":{"row":22,"column":60},"end":{"row":22,"column":61},"action":"insert","lines":["s"],"id":51}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["_"],"id":52},{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["o"]},{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["b"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["j"]}],[{"start":{"row":24,"column":4},"end":{"row":27,"column":4},"action":"remove","lines":["for post in posts: #list comprehension","        user_posts_list.append(get_post_details_dict(post))","","    "],"id":53}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"remove","lines":[" "],"id":54}],[{"start":{"row":22,"column":39},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"remove","lines":["    "],"id":56},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]},{"start":{"row":22,"column":39},"end":{"row":23,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":[" "],"id":57}],[{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"remove","lines":[" "],"id":58}],[{"start":{"row":22,"column":39},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":24,"column":9},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":8},"action":"remove","lines":["    "],"id":61},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":25,"column":0},"end":{"row":25,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588054733894,"hash":"35a15d60880993f8b14e21a54d5db333768e971d"}