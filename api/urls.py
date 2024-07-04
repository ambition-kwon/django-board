from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ExternalAPIClientView
from .views import StudentViewSet, ProfessorViewSet

router = DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'professor', ProfessorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('github/', ExternalAPIClientView.as_view())
]
