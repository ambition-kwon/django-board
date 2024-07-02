from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['GET'], url_path='student_professor')
    def student_professor(self, request):
        student_name = request.query_params.get('name')
        if not student_name:
            return Response({"error" : "name parameter is not included"}, status.HTTP_404_NOT_FOUND)
        student = get_object_or_404(Student, name=student_name)
        professor = student.professor
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)



