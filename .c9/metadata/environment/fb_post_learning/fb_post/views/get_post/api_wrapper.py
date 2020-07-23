{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/get_post/api_wrapper.py","ace":{"folds":[],"scrolltop":152.41891040122889,"scrollleft":0,"selection":{"start":{"row":0,"column":36},"end":{"row":0,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"state":"start","mode":"ace/mode/python"}},"hash":"269de224f8786a55e1e573448f3f646a608ded40","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["    # ---------MOCK IMPLEMENTATION---------",""],"id":3}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["from fb_post.utils import create_comment","","from raven.utils import json","from fb_post.constants import INVALID_COMMENT_CONTENT","from fb_post.constants import INVALID_POST","","from django_swagger_utils.drf_server.exceptions import BadRequest","from fb_post.validators import InvalidPostException","from fb_post.validators import InvalidCommentContent",""],"id":5}],[{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"remove","lines":["t"],"id":6},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"remove","lines":["n"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"remove","lines":["e"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"remove","lines":["m"]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"remove","lines":["m"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"remove","lines":["o"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"remove","lines":["c"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"remove","lines":["_"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"remove","lines":["e"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"remove","lines":["t"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"remove","lines":["a"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"remove","lines":["e"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"remove","lines":["r"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"remove","lines":["c"]}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["g"],"id":7},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["e"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["t"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["_"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["p"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["s"],"id":8},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["from fb_post.constants import INVALID_COMMENT_CONTENT",""],"id":9}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["from fb_post.validators import InvalidCommentContent",""],"id":10}],[{"start":{"row":14,"column":33},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["p"],"id":12},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["o"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["s"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["t"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["_"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["i"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":[" "],"id":13},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":[" "],"id":14},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["p"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["o"],"id":15},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["p"]}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":20},"action":"insert","lines":["kwargs"],"id":16}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":22},"action":"insert","lines":["[]"],"id":17}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":23},"action":"insert","lines":["''"],"id":18}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["p"],"id":19},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["o"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["s"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["t"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["_"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["i"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":31},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["t"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["r"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["y"]}],[{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":[":"],"id":21}],[{"start":{"row":17,"column":8},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["p"],"id":23},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["o"]},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["s"]},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["t"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["d"],"id":24},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["e"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["t"]},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["a"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["i"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["l"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["s"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["_"]},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["i"],"id":25},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["c"]},{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":[" "],"id":26},{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"insert","lines":["="]}],[{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":[" "],"id":27},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":[" "]},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":["g"]},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":["e"]},{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"remove","lines":["t"],"id":28},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"remove","lines":["e"]},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"remove","lines":["g"]},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"remove","lines":[" "]}],[{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["g"],"id":29},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":["e"]},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":["t"]},{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["_"]},{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"insert","lines":["p"]},{"start":{"row":18,"column":33},"end":{"row":18,"column":34},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":34},"end":{"row":18,"column":35},"action":"insert","lines":["s"],"id":30},{"start":{"row":18,"column":35},"end":{"row":18,"column":36},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":36},"end":{"row":18,"column":38},"action":"insert","lines":["()"],"id":31}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["p"],"id":32},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":["o"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["s"]},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["t"]},{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":["_"]},{"start":{"row":18,"column":42},"end":{"row":18,"column":43},"action":"insert","lines":["i"]},{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":[" "],"id":33},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["="]}],[{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"remove","lines":["="],"id":34},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"remove","lines":[" "]}],[{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":["="],"id":35},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["p"]},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"insert","lines":["o"]},{"start":{"row":18,"column":47},"end":{"row":18,"column":48},"action":"insert","lines":["s"]},{"start":{"row":18,"column":48},"end":{"row":18,"column":49},"action":"insert","lines":["t"]},{"start":{"row":18,"column":49},"end":{"row":18,"column":50},"action":"insert","lines":["_"]},{"start":{"row":18,"column":50},"end":{"row":18,"column":51},"action":"insert","lines":["i"]}],[{"start":{"row":18,"column":51},"end":{"row":18,"column":52},"action":"insert","lines":["d"],"id":36}],[{"start":{"row":18,"column":53},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":38}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["e"],"id":39},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["x"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":6},"action":"remove","lines":["ex"],"id":40},{"start":{"row":19,"column":4},"end":{"row":19,"column":14},"action":"insert","lines":["exceptions"]}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"remove","lines":["s"],"id":41},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"remove","lines":["n"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":["o"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":["i"]}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":[" "],"id":42}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["I"],"id":43},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":13},"action":"remove","lines":["In"],"id":44},{"start":{"row":19,"column":11},"end":{"row":19,"column":31},"action":"insert","lines":["InvalidPostException"]}],[{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"insert","lines":[":"],"id":45}],[{"start":{"row":19,"column":32},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":46},{"start":{"row":20,"column":0},"end":{"row":20,"column":8},"action":"insert","lines":["        "]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["r"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["a"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["i"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["s"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":[" "],"id":47},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["B"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":16},"action":"remove","lines":["Ba"],"id":48},{"start":{"row":20,"column":14},"end":{"row":20,"column":24},"action":"insert","lines":["BadRequest"]}],[{"start":{"row":20,"column":24},"end":{"row":20,"column":26},"action":"insert","lines":["()"],"id":49}],[{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["*"],"id":50}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":[" "],"id":51}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"remove","lines":[" "],"id":52}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":["I"],"id":53}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"remove","lines":["I"],"id":54},{"start":{"row":20,"column":26},"end":{"row":20,"column":38},"action":"insert","lines":["INVALID_POST"]}],[{"start":{"row":20,"column":39},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "],"id":56},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":57}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["p"],"id":58},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["o"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["s"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["t"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["_"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["i"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["d"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["c"]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"remove","lines":["c"],"id":59},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"remove","lines":["d"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"remove","lines":["i"]}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["d"],"id":60},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["e"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["t"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["a"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["i"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["l"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["s"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["i"],"id":61},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"remove","lines":["n"],"id":62},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"remove","lines":["i"]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["j"],"id":63},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["s"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["o"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":[" "],"id":64},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":[" "],"id":65},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["j"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["s"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["o"]}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["n"],"id":66},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["."]},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["d"]},{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"insert","lines":["u"]},{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["m"]},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"insert","lines":["p"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":34},"end":{"row":21,"column":36},"action":"insert","lines":["()"],"id":67}],[{"start":{"row":21,"column":35},"end":{"row":21,"column":52},"action":"insert","lines":["post_details_dict"],"id":68}],[{"start":{"row":20,"column":39},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":69},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "],"id":70},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":22,"column":53},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":71},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["r"]},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["s"]},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["p"]}],[{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"remove","lines":["p"],"id":72},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"remove","lines":["s"]}],[{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["e"],"id":73},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["s"]},{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["p"]},{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":["o"]},{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"insert","lines":["n"]},{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"insert","lines":["s"]},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":[" "],"id":74},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":[" "],"id":75},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"insert","lines":["H"]},{"start":{"row":23,"column":16},"end":{"row":23,"column":17},"action":"insert","lines":["t"]},{"start":{"row":23,"column":17},"end":{"row":23,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":18},"end":{"row":23,"column":19},"action":"insert","lines":["p"],"id":76},{"start":{"row":23,"column":19},"end":{"row":23,"column":20},"action":"insert","lines":["R"]},{"start":{"row":23,"column":20},"end":{"row":23,"column":21},"action":"insert","lines":["e"]},{"start":{"row":23,"column":21},"end":{"row":23,"column":22},"action":"insert","lines":["s"]},{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["p"]},{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["o"]},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"insert","lines":["n"]},{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"insert","lines":["s"]},{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":23,"column":27},"end":{"row":23,"column":29},"action":"insert","lines":["()"],"id":77}],[{"start":{"row":23,"column":28},"end":{"row":23,"column":45},"action":"insert","lines":["post_details_json"],"id":78}],[{"start":{"row":23,"column":45},"end":{"row":23,"column":46},"action":"insert","lines":["."],"id":79}],[{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"insert","lines":[" "],"id":80}],[{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"remove","lines":[" "],"id":81},{"start":{"row":23,"column":45},"end":{"row":23,"column":46},"action":"remove","lines":["."]}],[{"start":{"row":23,"column":45},"end":{"row":23,"column":46},"action":"insert","lines":[","],"id":82}],[{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"insert","lines":[" "],"id":83},{"start":{"row":23,"column":47},"end":{"row":23,"column":48},"action":"insert","lines":["s"]},{"start":{"row":23,"column":48},"end":{"row":23,"column":49},"action":"insert","lines":["t"]},{"start":{"row":23,"column":49},"end":{"row":23,"column":50},"action":"insert","lines":["a"]},{"start":{"row":23,"column":50},"end":{"row":23,"column":51},"action":"insert","lines":["t"]},{"start":{"row":23,"column":51},"end":{"row":23,"column":52},"action":"insert","lines":["u"]},{"start":{"row":23,"column":52},"end":{"row":23,"column":53},"action":"insert","lines":["s"]}],[{"start":{"row":23,"column":53},"end":{"row":23,"column":54},"action":"insert","lines":["="],"id":84},{"start":{"row":23,"column":54},"end":{"row":23,"column":55},"action":"insert","lines":["2"]},{"start":{"row":23,"column":55},"end":{"row":23,"column":56},"action":"insert","lines":["0"]},{"start":{"row":23,"column":56},"end":{"row":23,"column":57},"action":"insert","lines":["0"]}],[{"start":{"row":23,"column":58},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":85},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":86}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "],"id":87}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":88}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "],"id":89}],[{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":90},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["r"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["e"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["t"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["u"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["r"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["r"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"remove","lines":["n"],"id":91},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"remove","lines":["r"]}],[{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["n"],"id":92}],[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":[" "],"id":93},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["R"]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"remove","lines":["e"],"id":94},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"remove","lines":["R"]}],[{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["r"],"id":95},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["e"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":11},"end":{"row":25,"column":14},"action":"remove","lines":["res"],"id":96},{"start":{"row":25,"column":11},"end":{"row":25,"column":19},"action":"insert","lines":["response"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":97}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":98},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":99},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["d"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["j"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["a"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["n"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["g"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["o"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["."]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["h"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["t"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["p"],"id":100}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":[" "],"id":101},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["i"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["m"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["p"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["o"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["r"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":[" "],"id":102},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["H"]}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"remove","lines":["H"],"id":103},{"start":{"row":0,"column":24},"end":{"row":0,"column":36},"action":"insert","lines":["HttpResponse"]}]]},"timestamp":1588915659345}