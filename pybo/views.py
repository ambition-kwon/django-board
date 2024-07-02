from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    question_list = Question.objects.all().order_by('-created_at')
    context = {
        'question_list': question_list
    }
    # render 로 넘길 때는 무조건 dictionary 객체 여야함
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question_subject": question.subject,
        "question_content": question.content,
        "question_created_at": question.created_at,
        "question_id": question_id,
    }
    return render(request, "pybo/question_detail.html", context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answers.create(content=request.POST['content'])
