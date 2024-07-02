from django.http import HttpResponse
from .models import Question, Answer
from django.shortcuts import render


def index(request):
    question_list = Question.objects.all().order_by('-created_at')
    context = {
        'question_list': question_list
    }
    # render로 넘길 때는 무조건 딕셔너리 객체여야함
    return render(request, 'pybo/question_list.html', context)
