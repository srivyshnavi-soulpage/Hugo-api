from hugo.db.models import Project,ProjectAssignee
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
       model = Project
       fields = "__all__"


class ProjectAssigneeSerializer(serializers.ModelSerializer):
    class Meta:
       model = ProjectAssignee
       fields = "__all__"