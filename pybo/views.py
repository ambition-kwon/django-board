from django.http import HttpResponse
from .models import Question, Answer
from django.shortcuts import render, get_object_or_404


def index(request):
    question_list = Question.objects.all().order_by('-created_at')
    context = {
        'question_list': question_list
    }
    # render로 넘길 때는 무조건 딕셔너리 객체여야함
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question_subject": question.subject,
        "question_content": question.content,
        "question_created_at": question.created_at,
    }
    return render(request, "pybo/question_detail.html", context)
