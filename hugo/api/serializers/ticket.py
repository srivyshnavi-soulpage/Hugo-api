from hugo.db.models import Ticket,RequestTicket,TicketAvailability
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
       model = Ticket
       fields = "__all__"

class RequestTicketSerializer(serializers.ModelSerializer):
    class Meta:
       model = RequestTicket
       fields = "__all__"

class TicketAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
       model = TicketAvailability
       fields = "__all__"