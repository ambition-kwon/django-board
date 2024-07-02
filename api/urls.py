from django.urls import path, include
from .views import StudentViewSet, ProfessorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'professor', ProfessorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
