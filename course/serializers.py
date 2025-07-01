from rest_framework import serializers
from .models import Department, Instructor, Course


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class InstructorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )

    class Meta:
        model = Instructor
        fields = ['id', 'full_name', 'email', 'phone_number', 'department', 'department_id']


class CourseSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    department_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Department.objects.all(),
        write_only=True,
        source='departments'
    )
    instructor = InstructorSerializer(read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source='instructor', write_only=True
    )

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'departments',     
            'department_ids',  
            'instructor',
            'instructor_id',
            'start_date',
            'end_date'
        ]
