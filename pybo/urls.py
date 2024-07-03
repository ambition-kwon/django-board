from django.urls import path

from . import views

#alias 중복 방지를 위한 별칭 지정
app_name = 'pybo'

urlpatterns = [
    # name값은 별칭(alias) 지정. 즉, pybo/는 index라는 이름, pybo/int/는 detail이라는 이름.
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
