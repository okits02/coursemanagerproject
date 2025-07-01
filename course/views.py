from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Instructor, Course
from .serializers import DepartmentSerializer, InstructorSerializer, CourseSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name'] 


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id'] 


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = [
        'title',                   
        'instructor__id',          
        'departments__name'        
    ]
