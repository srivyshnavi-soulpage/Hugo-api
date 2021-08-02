from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404



from hugo.api.serializers import(
    ProjectSerializer,ProjectAssigneeSerializer
)
from hugo.db.models import(
    Project,User,ProjectAssignee
)
from django.http import HttpResponse,JsonResponse

class ProjectApi(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self,request, pk=None) :

        project = Project.objects.filter(id=pk)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        assignee = User.objects.get(id=pk)
        request.data["assignee"]= assignee.id
        print(pk)
        print(request.data)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # def get(self, request):
    #     queryset = Project.objects.all()
    #     serializer = ProjectSerializer(queryset, many=True)

    #     return render(
    #         context={
    #             "projects": queryset,
    
    #         },
    #     )


    


    
    # def post(self, request):
    #     serializer = ProjectSerializer(data=request.data)
    #     print(serializer.is_valid())
    #     if serializer.is_valid():
    #         project_instance = serializer.save()
    #         assignee_data = [
    #            {"employee": assignee, "project": project_instance.id}
    #            for assignee in request.data.getlist("assignees[]", [])
    #         ]
    #         assignee_serializer = ProjectAssigneeSerializer(
    #            data=assignee_data, many=True
    #        )
    #         if not assignee_serializer.is_valid():
    #            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         assignee_serializer.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    


class ProjectDetail(APIView):

    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        """
        Return  object if pk value present.
        """
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        """
        Return 
        """
        assignee = self.get_object(pk)

        serializer = ProjectSerializer(assignee)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def put(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        request.data["user"]= user.id
        print(pk)
        print(request.data)
        serializer = ProjectSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        project = Project.objects.get(id=pk)
        project.delete()
        return Response({"message": "Delete Success"}, status=status.HTTP_200_OK)






