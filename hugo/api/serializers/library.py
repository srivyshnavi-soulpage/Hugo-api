from hugo.db.models import Event,Holiday
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
       model = Event
       fields = "__all__"

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
       model = Holiday
       fields = "__all__"
