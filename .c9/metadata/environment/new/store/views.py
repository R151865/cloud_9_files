{"filter":false,"title":"views.py","tooltip":"/new/store/views.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["l"],"id":1},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["s"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["a"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["j"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["k"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["j"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["f"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["l"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["k"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["f"]},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":0},"end":{"row":24,"column":0},"action":"remove","lines":["from django.shortcuts import render, redirect","","import pytz","","from django.http import HttpResponse","","import datetime","from django.utils import timezone","#from django.template.response import TemplateResponse","","# Create your views here.","","","","def index(request):","    print('It is Timzone')lsajkjflkfl","   # print(request.GET['timezone'])","    #if request.method == 'POST' or request.method == 'GET':","    #    request.session['django_timezone']= request.POST['timezone']","    #    return redirect('/')","    #else:","    return render(request, 'temp.html',{'value':datetime.datetime.now(),'time1':timezone.now()})","","    #return render(request, 'temp.html',{'timezones':pytz.common_timezones})",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":7,"column":85},"action":"insert","lines":["from django.shortcuts import redirect, render","","def set_timezone(request):","    if request.method == 'POST':","        request.session['django_timezone'] = request.POST['timezone']","        return redirect('/')","    else:","        return render(request, 'template.html', {'timezones': pytz.common_timezones})"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":5},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["p"]}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["p"],"id":6},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":[" "]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["o"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["r"]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["f"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"],"id":7},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["p"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["o"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":8},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["p"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["y"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["t"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["z"]}],[{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"remove","lines":["e"],"id":9},{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"remove","lines":["t"]},{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"remove","lines":["a"]},{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"remove","lines":["l"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":36},"end":{"row":10,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589438669768,"hash":"79dd059886fcd48076dc2f2f4e76c9367d7f7934"}