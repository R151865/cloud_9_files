{"filter":false,"title":"store.py","tooltip":"/oop_submissions/OOP005/store.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":135,"column":9},"end":{"row":135,"column":10},"action":"remove","lines":[" "],"id":99},{"start":{"row":135,"column":8},"end":{"row":135,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":219,"column":0},"end":{"row":219,"column":2},"action":"insert","lines":["\"\""],"id":100}],[{"start":{"row":219,"column":2},"end":{"row":219,"column":3},"action":"insert","lines":["\""],"id":101}],[{"start":{"row":225,"column":7},"end":{"row":226,"column":0},"action":"insert","lines":["",""],"id":102}],[{"start":{"row":226,"column":0},"end":{"row":226,"column":2},"action":"insert","lines":["\"\""],"id":103}],[{"start":{"row":226,"column":2},"end":{"row":226,"column":3},"action":"insert","lines":["\""],"id":104}],[{"start":{"row":233,"column":0},"end":{"row":234,"column":0},"action":"insert","lines":["",""],"id":105}],[{"start":{"row":234,"column":0},"end":{"row":234,"column":2},"action":"insert","lines":["\"\""],"id":106}],[{"start":{"row":236,"column":8},"end":{"row":237,"column":0},"action":"insert","lines":["",""],"id":107}],[{"start":{"row":237,"column":0},"end":{"row":237,"column":2},"action":"insert","lines":["\"\""],"id":108}],[{"start":{"row":237,"column":2},"end":{"row":237,"column":3},"action":"insert","lines":["\""],"id":109}],[{"start":{"row":234,"column":2},"end":{"row":234,"column":3},"action":"insert","lines":["\""],"id":110}],[{"start":{"row":219,"column":0},"end":{"row":219,"column":3},"action":"remove","lines":["\"\"\""],"id":111}],[{"start":{"row":222,"column":0},"end":{"row":222,"column":3},"action":"insert","lines":["\"\"\""],"id":112}],[{"start":{"row":220,"column":49},"end":{"row":220,"column":50},"action":"remove","lines":["1"],"id":113},{"start":{"row":220,"column":48},"end":{"row":220,"column":49},"action":"remove","lines":["2"]}],[{"start":{"row":220,"column":48},"end":{"row":220,"column":49},"action":"insert","lines":["3"],"id":114},{"start":{"row":220,"column":49},"end":{"row":220,"column":50},"action":"insert","lines":["0"]}],[{"start":{"row":221,"column":58},"end":{"row":221,"column":59},"action":"remove","lines":["o"],"id":115},{"start":{"row":221,"column":57},"end":{"row":221,"column":58},"action":"remove","lines":["o"]}],[{"start":{"row":221,"column":57},"end":{"row":221,"column":58},"action":"insert","lines":["O"],"id":116},{"start":{"row":221,"column":58},"end":{"row":221,"column":59},"action":"insert","lines":["r"]}],[{"start":{"row":221,"column":59},"end":{"row":221,"column":60},"action":"insert","lines":["e"],"id":117}],[{"start":{"row":204,"column":0},"end":{"row":245,"column":3},"action":"remove","lines":["","store = Store()","item = Item(name=\"Oreo Biscuits\", price=30, category=\"Food\")","store.add_item(item)","item = Item(name=\"Boost Biscuits\", price=20, category=\"Food\")","store.add_item(item)","item = Item(name=\"ParleG Biscuits\", price=10, category=\"Food\")","store.add_item(item)","#print(store)","","\"\"\"","Oreo Biscuits@30-Food","Boost Biscuits@20-Food","ParleG Biscuits@10-Food","\"\"\"","","k = Query(field=\"price\", operation=\"GTE\", value=30)","query = Query(field=\"name\", operation=\"CONTAINS\", value=\"Ore\")","\"\"\"","q = store.filter(k, query) # should be able to give any number of Query objects as arguments","print(q)","print()","\"\"\"","","","results = store.exclude(k, query) # should be able to give any number of Query objects as arguments","print(results)","print()","#print(store)","","\"\"\"","k=q+results","print(k)","\"\"\"","\"\"\"","Oreo Biscuits@30-Food","ParleG Biscuits@10-Food","\"\"\"","","\"\"\"","Boost Biscuits@20-Food","\"\"\""],"id":118},{"start":{"row":204,"column":0},"end":{"row":226,"column":23},"action":"insert","lines":["store = Store()",">>> item = Item(name=\"Oreo Biscuits\", price=30, category=\"Food\")",">>> store.add_item(item)",">>> item = Item(name=\"Boost Biscuits\", price=20, category=\"Food\")",">>> store.add_item(item)",">>> item = Item(name=\"ParleG Biscuits\", price=10, category=\"Food\")",">>> store.add_item(item)",">>> print(store)","Oreo Biscuits@30-Food","Boost Biscuits@20-Food","ParleG Biscuits@10-Food",">>> query = Query(field=\"price\", operation=\"GT\", value=15)",">>> query = Query(field=\"name\", operation=\"CONTAINS\", value=\"oo\")","",">>> results = store.filter(query, query) # should be able to give any number of Query objects as arguments",">>> print(results)","Boost Biscuits@20-Food","","",">>> results = store.exclude(query, query) # should be able to give any number of Query objects as arguments",">>> print(results)","Oreo Biscuits@30-Food","ParleG Biscuits@10-Food"]}],[{"start":{"row":205,"column":3},"end":{"row":205,"column":4},"action":"remove","lines":[" "],"id":119},{"start":{"row":205,"column":2},"end":{"row":205,"column":3},"action":"remove","lines":[">"]},{"start":{"row":205,"column":1},"end":{"row":205,"column":2},"action":"remove","lines":[">"]},{"start":{"row":205,"column":0},"end":{"row":205,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":206,"column":2},"end":{"row":206,"column":3},"action":"remove","lines":[">"],"id":120},{"start":{"row":206,"column":1},"end":{"row":206,"column":2},"action":"remove","lines":[">"]}],[{"start":{"row":206,"column":1},"end":{"row":206,"column":2},"action":"remove","lines":[" "],"id":121},{"start":{"row":206,"column":0},"end":{"row":206,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":207,"column":3},"end":{"row":207,"column":4},"action":"remove","lines":[" "],"id":122},{"start":{"row":207,"column":2},"end":{"row":207,"column":3},"action":"remove","lines":[">"]},{"start":{"row":207,"column":1},"end":{"row":207,"column":2},"action":"remove","lines":[">"]},{"start":{"row":207,"column":0},"end":{"row":207,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":208,"column":3},"end":{"row":208,"column":4},"action":"remove","lines":[" "],"id":123},{"start":{"row":208,"column":2},"end":{"row":208,"column":3},"action":"remove","lines":[">"]},{"start":{"row":208,"column":1},"end":{"row":208,"column":2},"action":"remove","lines":[">"]},{"start":{"row":208,"column":0},"end":{"row":208,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":209,"column":3},"end":{"row":209,"column":4},"action":"remove","lines":[" "],"id":124},{"start":{"row":209,"column":2},"end":{"row":209,"column":3},"action":"remove","lines":[">"]},{"start":{"row":209,"column":1},"end":{"row":209,"column":2},"action":"remove","lines":[">"]},{"start":{"row":209,"column":0},"end":{"row":209,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":210,"column":3},"end":{"row":210,"column":4},"action":"remove","lines":[" "],"id":125},{"start":{"row":210,"column":2},"end":{"row":210,"column":3},"action":"remove","lines":[">"]},{"start":{"row":210,"column":1},"end":{"row":210,"column":2},"action":"remove","lines":[">"]},{"start":{"row":210,"column":0},"end":{"row":210,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":211,"column":3},"end":{"row":211,"column":4},"action":"remove","lines":[" "],"id":126},{"start":{"row":211,"column":2},"end":{"row":211,"column":3},"action":"remove","lines":[">"]},{"start":{"row":211,"column":1},"end":{"row":211,"column":2},"action":"remove","lines":[">"]},{"start":{"row":211,"column":0},"end":{"row":211,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":211,"column":12},"end":{"row":212,"column":0},"action":"insert","lines":["",""],"id":127}],[{"start":{"row":212,"column":0},"end":{"row":212,"column":2},"action":"insert","lines":["\"\""],"id":128}],[{"start":{"row":212,"column":2},"end":{"row":212,"column":3},"action":"insert","lines":["\""],"id":129}],[{"start":{"row":215,"column":23},"end":{"row":216,"column":0},"action":"insert","lines":["",""],"id":130}],[{"start":{"row":216,"column":0},"end":{"row":216,"column":2},"action":"insert","lines":["\"\""],"id":131}],[{"start":{"row":216,"column":2},"end":{"row":216,"column":3},"action":"insert","lines":["\""],"id":132}],[{"start":{"row":217,"column":3},"end":{"row":217,"column":4},"action":"remove","lines":[" "],"id":133},{"start":{"row":217,"column":2},"end":{"row":217,"column":3},"action":"remove","lines":[">"]},{"start":{"row":217,"column":1},"end":{"row":217,"column":2},"action":"remove","lines":[">"]},{"start":{"row":217,"column":0},"end":{"row":217,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":218,"column":3},"end":{"row":218,"column":4},"action":"remove","lines":[" "],"id":134},{"start":{"row":218,"column":2},"end":{"row":218,"column":3},"action":"remove","lines":[">"]},{"start":{"row":218,"column":1},"end":{"row":218,"column":2},"action":"remove","lines":[">"]},{"start":{"row":218,"column":0},"end":{"row":218,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":220,"column":3},"end":{"row":220,"column":4},"action":"remove","lines":[" "],"id":135},{"start":{"row":220,"column":2},"end":{"row":220,"column":3},"action":"remove","lines":[">"]},{"start":{"row":220,"column":1},"end":{"row":220,"column":2},"action":"remove","lines":[">"]},{"start":{"row":220,"column":0},"end":{"row":220,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":221,"column":3},"end":{"row":221,"column":4},"action":"remove","lines":[" "],"id":136},{"start":{"row":221,"column":2},"end":{"row":221,"column":3},"action":"remove","lines":[">"]},{"start":{"row":221,"column":1},"end":{"row":221,"column":2},"action":"remove","lines":[">"]},{"start":{"row":221,"column":0},"end":{"row":221,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":221,"column":14},"end":{"row":222,"column":0},"action":"insert","lines":["",""],"id":137}],[{"start":{"row":222,"column":0},"end":{"row":222,"column":2},"action":"insert","lines":["\"\""],"id":138}],[{"start":{"row":222,"column":2},"end":{"row":222,"column":3},"action":"insert","lines":["\""],"id":139}],[{"start":{"row":224,"column":0},"end":{"row":224,"column":2},"action":"insert","lines":["\"\""],"id":140}],[{"start":{"row":224,"column":2},"end":{"row":224,"column":3},"action":"insert","lines":["\""],"id":141}],[{"start":{"row":226,"column":3},"end":{"row":226,"column":4},"action":"remove","lines":[" "],"id":142},{"start":{"row":226,"column":2},"end":{"row":226,"column":3},"action":"remove","lines":[">"]},{"start":{"row":226,"column":1},"end":{"row":226,"column":2},"action":"remove","lines":[">"]},{"start":{"row":226,"column":0},"end":{"row":226,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":227,"column":3},"end":{"row":227,"column":4},"action":"remove","lines":[" "],"id":143},{"start":{"row":227,"column":2},"end":{"row":227,"column":3},"action":"remove","lines":[">"]},{"start":{"row":227,"column":1},"end":{"row":227,"column":2},"action":"remove","lines":[">"]},{"start":{"row":227,"column":0},"end":{"row":227,"column":1},"action":"remove","lines":[">"]}],[{"start":{"row":227,"column":14},"end":{"row":228,"column":0},"action":"insert","lines":["",""],"id":144}],[{"start":{"row":228,"column":0},"end":{"row":228,"column":2},"action":"insert","lines":["\"\""],"id":145}],[{"start":{"row":228,"column":2},"end":{"row":228,"column":3},"action":"insert","lines":["\""],"id":146}],[{"start":{"row":230,"column":23},"end":{"row":231,"column":0},"action":"insert","lines":["",""],"id":147}],[{"start":{"row":231,"column":0},"end":{"row":231,"column":2},"action":"insert","lines":["\"\""],"id":148}],[{"start":{"row":231,"column":2},"end":{"row":231,"column":3},"action":"insert","lines":["\""],"id":149}],[{"start":{"row":211,"column":12},"end":{"row":212,"column":0},"action":"insert","lines":["",""],"id":150},{"start":{"row":212,"column":0},"end":{"row":212,"column":1},"action":"insert","lines":["p"]},{"start":{"row":212,"column":1},"end":{"row":212,"column":2},"action":"insert","lines":["r"]},{"start":{"row":212,"column":2},"end":{"row":212,"column":3},"action":"insert","lines":["i"]},{"start":{"row":212,"column":3},"end":{"row":212,"column":4},"action":"insert","lines":["n"]},{"start":{"row":212,"column":4},"end":{"row":212,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":212,"column":5},"end":{"row":212,"column":7},"action":"insert","lines":["()"],"id":151}],[{"start":{"row":222,"column":14},"end":{"row":223,"column":0},"action":"insert","lines":["",""],"id":152},{"start":{"row":223,"column":0},"end":{"row":223,"column":1},"action":"insert","lines":["o"]},{"start":{"row":223,"column":1},"end":{"row":223,"column":2},"action":"insert","lines":["r"]}],[{"start":{"row":223,"column":1},"end":{"row":223,"column":2},"action":"remove","lines":["r"],"id":153},{"start":{"row":223,"column":0},"end":{"row":223,"column":1},"action":"remove","lines":["o"]}],[{"start":{"row":223,"column":0},"end":{"row":223,"column":1},"action":"insert","lines":["p"],"id":154},{"start":{"row":223,"column":1},"end":{"row":223,"column":2},"action":"insert","lines":["r"]},{"start":{"row":223,"column":2},"end":{"row":223,"column":3},"action":"insert","lines":["u"]},{"start":{"row":223,"column":3},"end":{"row":223,"column":4},"action":"insert","lines":["b"]}],[{"start":{"row":223,"column":3},"end":{"row":223,"column":4},"action":"remove","lines":["b"],"id":155},{"start":{"row":223,"column":2},"end":{"row":223,"column":3},"action":"remove","lines":["u"]}],[{"start":{"row":223,"column":2},"end":{"row":223,"column":3},"action":"insert","lines":["i"],"id":156},{"start":{"row":223,"column":3},"end":{"row":223,"column":4},"action":"insert","lines":["n"]},{"start":{"row":223,"column":4},"end":{"row":223,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":223,"column":5},"end":{"row":223,"column":7},"action":"insert","lines":["()"],"id":157}],[{"start":{"row":135,"column":7},"end":{"row":149,"column":7},"action":"remove","lines":[" \"\"\"","            if(query.operation=='IN'):","                for items in query.value:","                    for i in sb:","                        if(i.category==items):","                            pass","                        else:","                            self.list1.append(i)","                ","            elif(query.operation=='EQ'):","                for i in sb:","                    if (query.value==i.category or query.value==i.price or query.value==i.name):","                        pass","                    else:","       "],"id":158}],[{"start":{"row":135,"column":7},"end":{"row":135,"column":8},"action":"insert","lines":["\\"],"id":159}],[{"start":{"row":135,"column":7},"end":{"row":154,"column":7},"action":"remove","lines":["\\                 self.list1.append(i)","                ","            elif(query.operation=='GT' ):","                for i in sb:","                    if(i.price>query.value):","                      pass","                    else:","                        self.list1.append(i)","                ","            elif(query.operation=='GTE'):","                for i in sb:","                    if(i.price>=query.value):","                       pass","                    else:","                        self.list1.append(i)","                ","            elif(query.operation=='LT'):","                for i in sb:","                    if(i.price<query.value):","       "],"id":160}],[{"start":{"row":135,"column":7},"end":{"row":148,"column":7},"action":"remove","lines":["                pass","                    else:","                        self.list1.append(i)","                ","            elif(query.operation=='LTE'):","                for i in sb:","                    if(i.price<=query.value):","                       pass","                    else:","                        self.list1.append(i)","                ","            elif(query.operation=='STARTS_WITH'):","                for i in sb:","       "],"id":161},{"start":{"row":135,"column":7},"end":{"row":136,"column":0},"action":"insert","lines":["",""]},{"start":{"row":136,"column":0},"end":{"row":136,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":136,"column":7},"end":{"row":152,"column":7},"action":"remove","lines":["             if(i.name.startswith(query.value)):","                        pass","                    else:","                        self.list1.append(i)","                ","            elif(query.operation=='ENDS_WITH'):","                for i in sb:","                    if(i.name.endswith(query.value)):","                        pass","                    else:","                        self.list1.append(i)","                ","            elif(query.operation=='CONTAINS'):","                for i in sb:","                    if(query.value  in i.name):","                        pass","       "],"id":162}],[{"start":{"row":136,"column":7},"end":{"row":141,"column":7},"action":"remove","lines":["             else:","                        self.list1.append(i)","            sb=self.list1","        return Store(sb)","","       "],"id":163}],[{"start":{"row":136,"column":10},"end":{"row":136,"column":11},"action":"remove","lines":["\""],"id":164},{"start":{"row":136,"column":9},"end":{"row":136,"column":10},"action":"remove","lines":["\""]},{"start":{"row":136,"column":8},"end":{"row":136,"column":9},"action":"remove","lines":["\""]}],[{"start":{"row":152,"column":4},"end":{"row":152,"column":5},"action":"remove","lines":["y"],"id":165},{"start":{"row":152,"column":3},"end":{"row":152,"column":4},"action":"remove","lines":["r"]},{"start":{"row":152,"column":2},"end":{"row":152,"column":3},"action":"remove","lines":["e"]},{"start":{"row":152,"column":1},"end":{"row":152,"column":2},"action":"remove","lines":["u"]},{"start":{"row":152,"column":0},"end":{"row":152,"column":1},"action":"remove","lines":["q"]}],[{"start":{"row":152,"column":0},"end":{"row":152,"column":1},"action":"insert","lines":["k"],"id":166}],[{"start":{"row":155,"column":27},"end":{"row":155,"column":28},"action":"remove","lines":["y"],"id":167},{"start":{"row":155,"column":26},"end":{"row":155,"column":27},"action":"remove","lines":["r"]},{"start":{"row":155,"column":25},"end":{"row":155,"column":26},"action":"remove","lines":["e"]},{"start":{"row":155,"column":24},"end":{"row":155,"column":25},"action":"remove","lines":["u"]},{"start":{"row":155,"column":23},"end":{"row":155,"column":24},"action":"remove","lines":["q"]}],[{"start":{"row":155,"column":23},"end":{"row":155,"column":24},"action":"insert","lines":["k"],"id":168}],[{"start":{"row":162,"column":28},"end":{"row":162,"column":29},"action":"remove","lines":["y"],"id":169},{"start":{"row":162,"column":27},"end":{"row":162,"column":28},"action":"remove","lines":["r"]},{"start":{"row":162,"column":26},"end":{"row":162,"column":27},"action":"remove","lines":["e"]},{"start":{"row":162,"column":25},"end":{"row":162,"column":26},"action":"remove","lines":["u"]},{"start":{"row":162,"column":24},"end":{"row":162,"column":25},"action":"remove","lines":["q"]}],[{"start":{"row":162,"column":24},"end":{"row":162,"column":25},"action":"insert","lines":["k"],"id":170}],[{"start":{"row":162,"column":27},"end":{"row":162,"column":32},"action":"remove","lines":["query"],"id":171}],[{"start":{"row":162,"column":24},"end":{"row":162,"column":29},"action":"insert","lines":["query"],"id":172}],[{"start":{"row":162,"column":29},"end":{"row":162,"column":30},"action":"insert","lines":[","],"id":173}],[{"start":{"row":162,"column":31},"end":{"row":162,"column":32},"action":"remove","lines":[","],"id":174}],[{"start":{"row":162,"column":31},"end":{"row":162,"column":32},"action":"remove","lines":[" "],"id":175}],[{"start":{"row":122,"column":4},"end":{"row":122,"column":5},"action":"insert","lines":["#"],"id":176},{"start":{"row":122,"column":5},"end":{"row":122,"column":6},"action":"insert","lines":["i"]}],[{"start":{"row":122,"column":6},"end":{"row":122,"column":7},"action":"insert","lines":[" "],"id":177},{"start":{"row":122,"column":7},"end":{"row":122,"column":8},"action":"insert","lines":["d"]},{"start":{"row":122,"column":8},"end":{"row":122,"column":9},"action":"insert","lines":["i"]},{"start":{"row":122,"column":9},"end":{"row":122,"column":10},"action":"insert","lines":["d"]}],[{"start":{"row":122,"column":10},"end":{"row":122,"column":11},"action":"insert","lines":[" "],"id":178},{"start":{"row":122,"column":11},"end":{"row":122,"column":12},"action":"insert","lines":["n"]},{"start":{"row":122,"column":12},"end":{"row":122,"column":13},"action":"insert","lines":["o"]},{"start":{"row":122,"column":13},"end":{"row":122,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":122,"column":14},"end":{"row":122,"column":15},"action":"insert","lines":[" "],"id":179},{"start":{"row":122,"column":15},"end":{"row":122,"column":16},"action":"insert","lines":["u"]},{"start":{"row":122,"column":16},"end":{"row":122,"column":17},"action":"insert","lines":["d"]},{"start":{"row":122,"column":17},"end":{"row":122,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":122,"column":17},"end":{"row":122,"column":18},"action":"remove","lines":["n"],"id":180},{"start":{"row":122,"column":16},"end":{"row":122,"column":17},"action":"remove","lines":["d"]}],[{"start":{"row":122,"column":16},"end":{"row":122,"column":17},"action":"insert","lines":["n"],"id":181},{"start":{"row":122,"column":17},"end":{"row":122,"column":18},"action":"insert","lines":["d"]},{"start":{"row":122,"column":18},"end":{"row":122,"column":19},"action":"insert","lines":["e"]},{"start":{"row":122,"column":19},"end":{"row":122,"column":20},"action":"insert","lines":["r"]},{"start":{"row":122,"column":20},"end":{"row":122,"column":21},"action":"insert","lines":["s"]},{"start":{"row":122,"column":21},"end":{"row":122,"column":22},"action":"insert","lines":["t"]},{"start":{"row":122,"column":22},"end":{"row":122,"column":23},"action":"insert","lines":["a"]},{"start":{"row":122,"column":23},"end":{"row":122,"column":24},"action":"insert","lines":["n"]},{"start":{"row":122,"column":24},"end":{"row":122,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":122,"column":25},"end":{"row":122,"column":26},"action":"insert","lines":[" "],"id":182},{"start":{"row":122,"column":26},"end":{"row":122,"column":27},"action":"insert","lines":["w"]},{"start":{"row":122,"column":27},"end":{"row":122,"column":28},"action":"insert","lines":["a"]}],[{"start":{"row":122,"column":27},"end":{"row":122,"column":28},"action":"remove","lines":["a"],"id":183}],[{"start":{"row":122,"column":27},"end":{"row":122,"column":28},"action":"insert","lines":["h"],"id":184},{"start":{"row":122,"column":28},"end":{"row":122,"column":29},"action":"insert","lines":["a"]},{"start":{"row":122,"column":29},"end":{"row":122,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":122,"column":30},"end":{"row":122,"column":31},"action":"insert","lines":[" "],"id":185},{"start":{"row":122,"column":31},"end":{"row":122,"column":32},"action":"insert","lines":["i"]},{"start":{"row":122,"column":32},"end":{"row":122,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":122,"column":33},"end":{"row":122,"column":34},"action":"insert","lines":[" "],"id":186},{"start":{"row":122,"column":34},"end":{"row":122,"column":35},"action":"insert","lines":["g"]},{"start":{"row":122,"column":35},"end":{"row":122,"column":36},"action":"insert","lines":["o"]},{"start":{"row":122,"column":36},"end":{"row":122,"column":37},"action":"insert","lines":["i"]},{"start":{"row":122,"column":37},"end":{"row":122,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":122,"column":38},"end":{"row":122,"column":39},"action":"insert","lines":[" "],"id":187}],[{"start":{"row":122,"column":38},"end":{"row":122,"column":39},"action":"remove","lines":[" "],"id":188},{"start":{"row":122,"column":37},"end":{"row":122,"column":38},"action":"remove","lines":["n"]}],[{"start":{"row":122,"column":37},"end":{"row":122,"column":38},"action":"insert","lines":["n"],"id":189},{"start":{"row":122,"column":38},"end":{"row":122,"column":39},"action":"insert","lines":["g"]}],[{"start":{"row":122,"column":39},"end":{"row":122,"column":40},"action":"insert","lines":[" "],"id":190},{"start":{"row":122,"column":40},"end":{"row":122,"column":41},"action":"insert","lines":["o"]},{"start":{"row":122,"column":41},"end":{"row":122,"column":42},"action":"insert","lines":["n"]}],[{"start":{"row":122,"column":42},"end":{"row":122,"column":43},"action":"insert","lines":[" "],"id":191},{"start":{"row":122,"column":43},"end":{"row":122,"column":44},"action":"insert","lines":["h"]},{"start":{"row":122,"column":44},"end":{"row":122,"column":45},"action":"insert","lines":["e"]},{"start":{"row":122,"column":45},"end":{"row":122,"column":46},"action":"insert","lines":["r"]},{"start":{"row":122,"column":46},"end":{"row":122,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":147,"column":3},"end":{"row":148,"column":0},"action":"insert","lines":["",""],"id":192}],[{"start":{"row":147,"column":2},"end":{"row":147,"column":3},"action":"remove","lines":["\""],"id":193},{"start":{"row":147,"column":1},"end":{"row":147,"column":2},"action":"remove","lines":["\""]},{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":137,"column":0},"end":{"row":137,"column":2},"action":"insert","lines":["\"\""],"id":194}],[{"start":{"row":137,"column":2},"end":{"row":137,"column":3},"action":"insert","lines":["\""],"id":195}],[{"start":{"row":152,"column":2},"end":{"row":152,"column":3},"action":"remove","lines":["\""],"id":196},{"start":{"row":152,"column":1},"end":{"row":152,"column":2},"action":"remove","lines":["\""]},{"start":{"row":152,"column":0},"end":{"row":152,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":159,"column":2},"end":{"row":159,"column":3},"action":"remove","lines":["\""],"id":197},{"start":{"row":159,"column":1},"end":{"row":159,"column":2},"action":"remove","lines":["\""]},{"start":{"row":159,"column":0},"end":{"row":159,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":161,"column":2},"end":{"row":161,"column":3},"action":"remove","lines":["\""],"id":198},{"start":{"row":161,"column":1},"end":{"row":161,"column":2},"action":"remove","lines":["\""]},{"start":{"row":161,"column":0},"end":{"row":161,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":165,"column":2},"end":{"row":165,"column":3},"action":"remove","lines":["\""],"id":199},{"start":{"row":165,"column":1},"end":{"row":165,"column":2},"action":"remove","lines":["\""]},{"start":{"row":165,"column":0},"end":{"row":165,"column":1},"action":"remove","lines":["\""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":165,"column":0},"end":{"row":165,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1582191831757,"hash":"3e819b5d3bd8dd9b46707403c159bd0dbcce47ec"}