{"filter":false,"title":"section_storage_implementation.py","tooltip":"/ib_miniprojects_backend/essentials_kit_management/storages/section_storage_implementation.py","undoManager":{"mark":40,"position":40,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["from essentials_kit_management.interactors.storages.item_storage_interface \\","    import ItemStorageInterface","","from essentials_kit_management.models import Item","","class ItemStorageImplementation(ItemStorageInterface):","","    def are_they_valid_item_ids(self, item_ids):","        item_ids = list(set(item_ids))","        count = len(item_ids)","","        objs_count = Item.objects.filter(id__in=item_ids).count()","","        are_all_valid_item_ids = objs_count == count","        return are_all_valid_item_ids",""],"id":1}],[{"start":{"row":0,"column":55},"end":{"row":0,"column":56},"action":"remove","lines":["m"],"id":2},{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"remove","lines":["e"]},{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"remove","lines":["t"]},{"start":{"row":0,"column":52},"end":{"row":0,"column":53},"action":"remove","lines":["i"]}],[{"start":{"row":0,"column":52},"end":{"row":0,"column":53},"action":"insert","lines":["s"],"id":3},{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"insert","lines":["e"]},{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"insert","lines":["c"]},{"start":{"row":0,"column":55},"end":{"row":0,"column":56},"action":"insert","lines":["t"]},{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"insert","lines":["i"]},{"start":{"row":0,"column":57},"end":{"row":0,"column":58},"action":"insert","lines":["o"]},{"start":{"row":0,"column":58},"end":{"row":0,"column":59},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["m"],"id":4},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["t"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":["I"]}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["S"],"id":5},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["e"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["c"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["t"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["i"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["o"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":48},"end":{"row":3,"column":49},"action":"remove","lines":["m"],"id":6},{"start":{"row":3,"column":47},"end":{"row":3,"column":48},"action":"remove","lines":["e"]},{"start":{"row":3,"column":46},"end":{"row":3,"column":47},"action":"remove","lines":["t"]},{"start":{"row":3,"column":45},"end":{"row":3,"column":46},"action":"remove","lines":["I"]}],[{"start":{"row":3,"column":45},"end":{"row":3,"column":46},"action":"insert","lines":["S"],"id":7},{"start":{"row":3,"column":46},"end":{"row":3,"column":47},"action":"insert","lines":["e"]},{"start":{"row":3,"column":47},"end":{"row":3,"column":48},"action":"insert","lines":["c"]},{"start":{"row":3,"column":48},"end":{"row":3,"column":49},"action":"insert","lines":["t"]},{"start":{"row":3,"column":49},"end":{"row":3,"column":50},"action":"insert","lines":["i"]},{"start":{"row":3,"column":50},"end":{"row":3,"column":51},"action":"insert","lines":["o"]},{"start":{"row":3,"column":51},"end":{"row":3,"column":52},"action":"insert","lines":["n"]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":10},"action":"remove","lines":["Item"],"id":8},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["S"]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["S"],"id":9},{"start":{"row":5,"column":6},"end":{"row":5,"column":13},"action":"insert","lines":["Section"]}],[{"start":{"row":5,"column":35},"end":{"row":5,"column":39},"action":"remove","lines":["Item"],"id":10},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":["S"]}],[{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"remove","lines":["S"],"id":11},{"start":{"row":5,"column":35},"end":{"row":5,"column":42},"action":"insert","lines":["Section"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["m"],"id":12},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"remove","lines":["e"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"remove","lines":["t"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"remove","lines":["i"]}],[{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["s"],"id":13},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["e"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["c"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":31},"action":"remove","lines":["are_they_valid_sect_ids"],"id":14},{"start":{"row":7,"column":8},"end":{"row":7,"column":34},"action":"insert","lines":["are_they_valid_section_ids"]}],[{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"remove","lines":["m"],"id":15},{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"remove","lines":["e"]},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"remove","lines":["t"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"remove","lines":["i"]}],[{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["s"],"id":16},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":41},"end":{"row":7,"column":43},"action":"remove","lines":["se"],"id":17},{"start":{"row":7,"column":41},"end":{"row":7,"column":48},"action":"insert","lines":["section"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["m"],"id":18},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["e"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["t"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["i"]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["s"],"id":19},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":14},"action":"remove","lines":["se_ids"],"id":20},{"start":{"row":8,"column":8},"end":{"row":8,"column":19},"action":"insert","lines":["section_ids"]}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"remove","lines":["m"],"id":21},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["e"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["t"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["i"]}],[{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["s"],"id":22},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":31},"end":{"row":8,"column":37},"action":"remove","lines":["se_ids"],"id":23},{"start":{"row":8,"column":31},"end":{"row":8,"column":42},"action":"insert","lines":["section_ids"]}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["m"],"id":24},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["e"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["t"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["i"]}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["s"],"id":25},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":26},"action":"remove","lines":["se_ids"],"id":26},{"start":{"row":9,"column":20},"end":{"row":9,"column":31},"action":"insert","lines":["section_ids"]}],[{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"remove","lines":["m"],"id":27},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"remove","lines":["e"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"remove","lines":["t"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":["I"]}],[{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["S"],"id":28}],[{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":["S"],"id":29},{"start":{"row":11,"column":21},"end":{"row":11,"column":28},"action":"insert","lines":["Section"]}],[{"start":{"row":11,"column":54},"end":{"row":11,"column":55},"action":"remove","lines":["m"],"id":30},{"start":{"row":11,"column":53},"end":{"row":11,"column":54},"action":"remove","lines":["e"]},{"start":{"row":11,"column":52},"end":{"row":11,"column":53},"action":"remove","lines":["t"]},{"start":{"row":11,"column":51},"end":{"row":11,"column":52},"action":"remove","lines":["i"]}],[{"start":{"row":11,"column":51},"end":{"row":11,"column":52},"action":"insert","lines":["e"],"id":31}],[{"start":{"row":11,"column":51},"end":{"row":11,"column":52},"action":"remove","lines":["e"],"id":32}],[{"start":{"row":11,"column":51},"end":{"row":11,"column":52},"action":"insert","lines":["s"],"id":33}],[{"start":{"row":11,"column":51},"end":{"row":11,"column":56},"action":"remove","lines":["s_ids"],"id":34},{"start":{"row":11,"column":51},"end":{"row":11,"column":62},"action":"insert","lines":["section_ids"]}],[{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["m"],"id":35},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["e"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["t"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["i"]}],[{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["s"],"id":36},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["e"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["c"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["t"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["i"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["o"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["m"],"id":37},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["e"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["t"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["i"]}],[{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["s"],"id":38},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["c"]}],[{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["c"],"id":39}],[{"start":{"row":14,"column":15},"end":{"row":14,"column":34},"action":"remove","lines":["are_all_valid_s_ids"],"id":40},{"start":{"row":14,"column":15},"end":{"row":14,"column":40},"action":"insert","lines":["are_all_valid_section_ids"]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":41}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":15},"end":{"row":15,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":70,"mode":"ace/mode/python"}},"timestamp":1591390370221,"hash":"e2e27acf86900631ee8b6e40d726ce525e9f2472"}