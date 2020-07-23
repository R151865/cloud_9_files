# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
  

def get_list_of_questions(request):
    latest_question_list = Question.objects.all()
    context={'latest_question_list':latest_question_list,}
    return render(request,'get_list_of_questions.html',context)
    
def create_question(request):
    if request.method=='GET':
        return render(request,"create_question_form.html")
    elif request.method=='POST':
        create_text=request.POST.get('question')
        create_answer=request.POST.get('answer')
        
        if len(create_text)>0 and len(create_answer)>0:
            question=Question(text=create_text,answer=create_answer)
            question.save()
            return render(request,"create_question_success.html")
        else:
            return render(request,"create_question_failure.html")

    
def get_question(request,question_id):
    question=Question.objects.get(pk=question_id)
    context={'question':question}
    return render(request,"each_question_form.html",context)

def update_question(request,question_id):
        upd_text=request.POST.get('question')
        upd_answer=request.POST.get('answer')
        
        if len(upd_text)>0 and len(upd_answer)>0 :
            question=Question.objects.get(pk=question_id)
            question.text=upd_text
            question.answer=upd_answer
            question.save()
            return render(request,'update_question_success.html')
        else:
            return render(request,'update_question_failure.html')
        
            

def delete_question(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
        
        
    except Question.DoesNotExist:
        return render(request,'delete_question_failure.html')
        
    question.delete()
    return render(request,'delete_question_success.html')
    
    
    
#for example purpose
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    """