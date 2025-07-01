from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, InstructorViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'instructors', InstructorViewSet, basename='instructor')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
]
