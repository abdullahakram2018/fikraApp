from django.shortcuts import render
from accountapp.models import Currency
from accountapp.serializers import CurrencySerializer
from userapp.serializer import RegisterSerializer,ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView 
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

# Create your views here.



class UserListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,format=None):
        user = request.user
        profile = Profile.objects.get(user=user.id)
        serialized_users = ProfileSerializer(profile, many=True)
        return Response(serialized_users.data)

  
 
@api_view(['POST'])
def register_api(request,instance=None,created=False, **kwargs):
    serialize_user = RegisterSerializer(data=request.data)
    if serialize_user.is_valid(raise_exception=True):
         serialize_user.save()
         return Response(serialize_user.data,status=status.HTTP_201_CREATED)
    return Response(serialize_user.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def user_detail(request, pk):
  
    """
    Retrieve, update or delete a code users.
    """
    try:
        
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        permission_classes = (IsAuthenticated,)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']    
    profile = Profile.objects.get(user=user.id)   
    profiledata = ProfileSerializer(profile)  
    users = request.user    
    token, created = Token.objects.get_or_create(user=user)    
    if profile.success == True:  
        return Response({   
            'token':token.key,
            'profile':profiledata.data,
        })
    return Response({'error': 'not Success'},status=400)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def user(request):
    
    user = request.user
    profile = Profile.objects.get(user=user.id)
    serializer = ProfileSerializer(profile,many=True)
    return Response(serializer.data)
   