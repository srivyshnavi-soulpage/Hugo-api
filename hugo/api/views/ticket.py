from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404



from hugo.api.serializers import(
    TicketSerializer,RequestTicketSerializer,TicketAvailabilitySerializer
)
from hugo.db.models import(
    Ticket,RequestTicket,TicketAvailability
)
from django.http import HttpResponse,JsonResponse

class TicketApi(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        # ticket = Ticket.objects.get(id=pk)
        # request.data["ticket"]= ticket.id
        # print(pk)
        # print(request.data)
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TicketDetail(APIView):
    """
   Retrieve, delete a Restaurant
   """


    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Return restaurant object if pk value present.
        """
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Restaurant.
        """
        ticket = self.get_object(pk)

        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        ticket = self.get_object(pk)
        print(ticket)
        print(request.data)
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        ticket = self.get_object(pk)
        ticket.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)



class RequestTicketApi(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

           req = RequestTicket.objects.filter(id=pk)
           serializer = RequestTicketSerializer(req, many=True)
           return Response(serializer.data)

    def post(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        request.data["ticket"]= ticket.id
        print(pk)
        print(request.data)
        serializer = RequestTicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
            try:
              return RequestTicket.objects.get(pk=pk)
            except RequestTicket.DoesNotExist:
             raise Http404

    def put(self, request, pk, format=None):
        
        # ticket = Ticket.objects.get(id=pk)
        # request.data["ticket"]= ticket.id
        try:
            ticket =Ticket.objects.get(id=pk)
        except Ticket.DoesNotExist:
            ticket = None
        req = self.get_object(pk)
        serializer = RequestTicketSerializer(req ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk, format=None):
        req = self.get_object(pk)
        req.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)

class RequestTicketDetail(APIView):
    """
    A view for viewing List of Request Tickets
    """
    def get(self,request, format=None):
        
       req = RequestTicket.objects.all()
       serializer = RequestTicketSerializer(req, many=True)
       return Response(serializer.data)



class TicketAvailabilityApi(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

           req = TicketAvailability.objects.filter(id=pk)
           serializer =TicketAvailabilitySerializer(req, many=True)
           return Response(serializer.data)

    def post(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        request.data["ticket"]= ticket.id
        print(pk)
        print(request.data)
        serializer = TicketAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
            try:
              return TicketAvailability.objects.get(pk=pk)
            except TicketAvailability.DoesNotExist:
             raise Http404

    def put(self, request, pk, format=None):
        
        # ticket = Ticket.objects.get(id=pk)
        # request.data["ticket"]= ticket.id
        try:
            ticket =Ticket.objects.get(id=pk)
        except Ticket.DoesNotExist:
            ticket = None
        req = self.get_object(pk)
        serializer = TicketAvailabilitySerializer(req ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk, format=None):
        req = self.get_object(pk)
        req.delete()
        return Response({"message": "Delete Success"},status=status.HTTP_200_OK)

class TicketAvailabilityDetail(APIView):
    """
    A view for viewing List of Request Tickets
    """
    def get(self,request, format=None):
        
       req = TicketAvailability.objects.all()
       serializer = TicketAvailabilitySerializer(req, many=True)
       return Response(serializer.data)

