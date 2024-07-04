import json

import requests
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Professor, Student
from .serializers import ProfessorSerializer, StudentSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    @action(detail=False, methods=['GET'], url_path='students_by_professor_name')
    def students_by_professor_name(self, request):
        professor_name = request.query_params.get('name')
        if not professor_name:
            return Response({"error" : "name parameter is not included"}, status.HTTP_404_NOT_FOUND)
        professor = get_object_or_404(Professor, name=professor_name)
        students = professor.students.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'], url_path='modify_professor_age')
    @transaction.atomic
    def modify_professor_age(self, request, pk=None):
        professor = get_object_or_404(self.get_queryset(), id=pk)
        professor.age = request.data.get('age')
        professor.save()
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['POST'], url_path='delete_professor_name')
    @transaction.atomic
    def delete_professor_name(self, request):
        name = request.data.get('name')
        print(name)
        if not name:
            return Response({"error": "Name parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        professor = self.get_queryset().filter(name=name)
        print(professor)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['DELETE'], url_path='delete_professors_by_age')
    @transaction.atomic
    def delete_professors_by_age(self, request):
        age = request.data.get('age')
        if not age:
            return Response({"error": "Age parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        professors = self.get_queryset().filter(age=age)
        deleted_count = professors.delete()[0]
        return Response({"deleted_count": deleted_count}, status=status.HTTP_204_NO_CONTENT)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ExternalAPIClientView(APIView):
    def get(self, request):
        external_url = "https://api.github.com/users/ambition-kwon"
        response = requests.get(external_url)
        print(json.dumps(response.text, indent=4))
        return Response(response.json())


