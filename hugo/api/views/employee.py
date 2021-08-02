from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404



from hugo.api.serializers import(
    UserSerializer,EmployeeSerializer,EmploymentSerializer,EmployDocsSerializer,EducationSerializer,
    EducationDocsSerializer,InternshipSerializer
)
from hugo.db.models import(
    User,Employee,Employment,EmployDocs,Education,EducationDocs,Internship
)
# import csv
from django.http import HttpResponse,JsonResponse

class EmployeeApi(APIView):
    #Viewing
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None):
        #return list 
        employee =Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    

    def post(self, request,pk=None):
        #create 

        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    """
   Retrieve, delete 
   """


    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return 
        """
        employee = self.get_object(pk)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        employee = self.get_object(pk)
        print(employee)
        print(request.data)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        employee = self.get_object(pk)
        employee.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)




class EmploymentApi(APIView):
    #Viewing
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None):
        #return list 
        employment =Employment.objects.all()
        serializer = EmploymentSerializer(employment,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    

    def post(self, request,pk=None):
        #create 

        serializer=EmploymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmploymentDetail(APIView):
    """
   Retrieve, delete 
   """


    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return Employment.objects.get(pk=pk)
        except Employment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return 
        """
        employment = self.get_object(pk)

        serializer = EmploymentSerializer(employment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        employment = self.get_object(pk)
        print(employment)
        print(request.data)
        serializer = EmploymentSerializer(employment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        employment = self.get_object(pk)
        employment.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)



class EmployDocsApi(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

        employdocs = EmployDocs.objects.all()
        serializer = EmployDocsSerializer(employdocs, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        employment = Employment.objects.get(id=pk)
        request.data["employment"]= employment.id
        print(pk)
        print(request.data)
        serializer = EmployDocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployDocsDetail(APIView):

    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return EmployDocs.objects.get(pk=pk)
        except EmployDocs.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        """
        Return 
        """
        employee = self.get_object(pk)

        serializer = EmployDocsSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def put(self, request, pk, format=None):
        employee = Employee.objects.get(id=pk)
        request.data['employee'] = employee.id
        #employdoc=self.get_object(pk)
        serializer =EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        print(pk)
        """
        Delete.
        """
        employdocs = EmployDocs.objects.get(id=pk)
        employdocs.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)


class EducationApi(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

        education = Education.objects.all()
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        education = Employee.objects.get(id=pk)
        request.data["education"]= education.id
        print(pk)
        print(request.data)
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationDetail(APIView):

    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return Education.objects.get(pk=pk)
        except Education.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        """
        Return 
        """
        employee = self.get_object(pk)

        serializer = EducationSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def put(self, request, pk, format=None):
        education = Employee.objects.get(id=pk)
        request.data['education'] = education.id
        #employdoc=self.get_object(pk)
        serializer =EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        education = Education.objects.get(id=pk)
        education.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)

class EducationDocsApi(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

        educationdocs = EducationDocs.objects.all()
        
        serializer = EducationDocsSerializer(educationdocs, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        education = Education.objects.get(id=pk)
        request.data["education"]= education.id
        print(pk)
        print(request.data)
        serializer = EducationDocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationDocsDetail(APIView):

    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return EducationDocs.objects.get(pk=pk)
        except EducationDocs.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        """
        Return 
        """
        education = self.get_object(pk)

        serializer = EducationDocsSerializer(education)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def put(self, request, pk, format=None):
        education = Education.objects.get(id=pk)
        request.data['education'] = education.id
        #employdoc=self.get_object(pk)
        serializer =EducationDocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        print(pk)
        """
        Delete.
        """
        educationdocs = EducationDocs.objects.get(id=pk)
        educationdocs.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)



class InternshipApi(APIView):
    #Viewing
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None):
        #return list 
        internship =Internship.objects.all()
        serializer = InternshipSerializer(internship,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    

    def post(self, request,pk=None):
        #create 

        serializer=InternshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





class InternshipDetail(APIView):
    """
   Retrieve, delete 
   """


    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return Internship.objects.get(pk=pk)
        except Internship.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return 
        """
        internship = self.get_object(pk)

        serializer = InternshipSerializer(internship)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        internship = self.get_object(pk)
        print(internship)
        print(request.data)
        serializer = InternshipSerializer(internship, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        internship = self.get_object(pk)
        internship.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)
