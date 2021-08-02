from hugo.db.models import Employee,Employment,EmployDocs,Education,EducationDocs,Internship
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Employee
       fields = "__all__"

class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields="__all__"

class EmployDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployDocs
        fields="__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields="__all__"


class EducationDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDocs
        fields="__all__"


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
       model = Internship
       fields = "__all__"
