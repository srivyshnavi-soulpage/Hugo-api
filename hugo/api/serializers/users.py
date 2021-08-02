from hugo.db.models import User,Salary
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields="__all__"


class SalarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Salary
        fields="__all__"