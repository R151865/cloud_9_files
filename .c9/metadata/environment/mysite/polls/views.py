{"changed":true,"filter":false,"title":"views.py","tooltip":"/mysite/polls/views.py","value":"","undoManager":{"mark":22,"position":23,"stack":[[{"start":{"row":14,"column":58},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":1},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["p"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["r"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["i"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["n"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":11},"action":"insert","lines":["()"],"id":2}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"remove","lines":[")"],"id":3},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"remove","lines":["("]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"remove","lines":["t"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"remove","lines":["n"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"remove","lines":["i"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"remove","lines":["r"]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["p"]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":58},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["\"\""],"id":5}],[{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["\""],"id":6},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["\""]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["\""]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["\""]}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":6},"action":"remove","lines":["\"\"\""],"id":7}],[{"start":{"row":36,"column":70},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "],"id":9}],[{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":3},"action":"insert","lines":["\"\"\""],"id":11}],[{"start":{"row":38,"column":2},"end":{"row":38,"column":3},"action":"remove","lines":["\""],"id":12},{"start":{"row":38,"column":1},"end":{"row":38,"column":2},"action":"remove","lines":["\""]},{"start":{"row":38,"column":0},"end":{"row":38,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"remove","lines":["\""],"id":13},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"remove","lines":["\""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["#"],"id":14}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["\"\""],"id":15}],[{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":["\""],"id":16},{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["\""]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["\""],"id":17}],[{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["\""],"id":18}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":6},"action":"remove","lines":["\"\"\""],"id":19}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":3},"action":"insert","lines":["\"\"\""],"id":20}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["#"],"id":21}],[{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"remove","lines":["\""],"id":22},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"remove","lines":["\""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":["\""]},{"start":{"row":8,"column":36},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":2},"end":{"row":37,"column":3},"action":"remove","lines":["\""],"id":23},{"start":{"row":37,"column":1},"end":{"row":37,"column":2},"action":"remove","lines":["\""]},{"start":{"row":37,"column":0},"end":{"row":37,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":0,"column":0},"end":{"row":37,"column":0},"action":"remove","lines":["from django.shortcuts import get_object_or_404,render","","# Create your views here.","from django.http import Http404","from django.shortcuts import render","from .models import Question,Choice","","from django.template import loader","from django.http import HttpResponse","","def index(request):","    latest_question_list = Question.objects.order_by('-pub_date')[:5]","    output = ', '.join([q.question_text for q in latest_question_list])","    template=loader.get_template('polls/index.html')","    context={'latest_question_list':latest_question_list,}","    return HttpResponse(template.render(context,request))","    ","    ","    ","def detail(request, question_id):","    latest_question_list = Choice.objects.all()","    template=loader.get_template('polls/items.html')","    context={'latest_question_list':latest_question_list}","    return HttpResponse(template.render(context,request))","   ","    ","    ","    ","    return HttpResponse(\"You're looking at question %s.\" % question_id)","","def results(request, question_id):","    response = \"You're looking at the results of question %s.\"","    return HttpResponse(response % question_id)","","def vote(request, question_id):","    return HttpResponse(\"You're voting on question %s.\" % question_id)","",""],"id":24}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584010611561}