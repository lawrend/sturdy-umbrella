from django.shortcuts import render
from django.http import HttpResponse

#loader is not needed if using the render shortcut
from django.template import loader

from .models import Question

"""
the following can be rewritten with render
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = { 'latest_question_list' : latest_question_list }
    return HttpResponse(template.render(context, request))
"""

#rewriting the above method
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list' : latest_question_list }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(request, question_id):
    response = "you are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)

