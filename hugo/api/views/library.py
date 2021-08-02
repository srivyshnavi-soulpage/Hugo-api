from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404



from hugo.api.serializers import(
    EventSerializer,HolidaySerializer
)
from hugo.db.models import(
    Event,Holiday
)

from django.http import HttpResponse,JsonResponse


# from django.http import HttpResponse,JsonResponse


# from rest_framework import mixins, generics
# from hugo.db.models import Event
# from hugo.api.serializers import EventSerializer

# class EventApi(mixins.ListModelMixin, 
#                       mixins.CreateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):

#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



class EventApi(APIView):
    #Viewing
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None):
        #return list 
        event =Event.objects.all()
        serializer = EventSerializer(event,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    

    def post(self, request,pk=None):
        #create 

        serializer=EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class EventDetail(APIView):
    """ 
    Retrieve, delete 
    """


    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return 
        """
        events = self.get_object(pk)

        serializer = EventSerializer(events)
        print(serializer.data)
        return Response(serializer.data)


    def put(self, request, pk, format=None):

        events = self.get_object(pk)
        print(events)
        print(request.data)
        serializer = EventSerializer(events, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        events = self.get_object(pk)
        events.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)



class HolidayApi(APIView):
    #Viewing
    permission_classes = [IsAuthenticated]
    def get(self, request):
        #return list 
        holiday =Holiday.objects.all()
        serializer = HolidaySerializer(holiday,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    

    def post(self, request):
        #create 

        serializer=HolidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class HolidayDetail(APIView):
    """
   Retrieve, delete a Restaurant
   """


    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Return restaurant object if pk value present.
        """
        try:
            return Holiday.objects.get(pk=pk)
        except Holiday.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return Restaurant.
        """
        holiday = self.get_object(pk)

        serializer = HolidaySerializer(holiday)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        holiday = self.get_object(pk)
        print(holiday)
        print(request.data)
        serializer = HolidaySerializer(holiday, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        holiday = self.get_object(pk)
        holiday.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)

