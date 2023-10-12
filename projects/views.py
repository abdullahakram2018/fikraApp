from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response

from projects.models import *
from projects.serializers import *
# Create your views here.

@api_view(['GET', 'PUT', 'DELETE','POST'])
@permission_classes((IsAuthenticated, ))
def project(request):
 
    try:
        project_id = request.POST['project_id']
        project = Project.objects.filter(id=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project,many=True)

        return Response({"detailproject":serializer.data})
    
    elif request.method == 'POST':
        serialize = ProjectSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True) :
            
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save(entry=Project.objects.get(id=project_id))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE','POST'])
@permission_classes((IsAuthenticated, ))
def branch(request):

    try:
        project_id = request.POST['project_id']
        branch_id = request.POST['branch_id']
        project = Branch.objects.filter(project=project_id)
        branch = Branch.objects.filter(id=branch_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(branch,many=True)

        return Response({"detailbranch":serializer.data})
    
    elif request.method == 'POST':
        serialize = BranchSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True) :
            serialize.save(project=Project.objects.get(id=project_id))
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save(project=Project.objects.get(id=project_id))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)