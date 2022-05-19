from ast import Raise
from yaml import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User
from user.serializers import UserSerializer

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"message": "Invalid Data"})
    return Response(serializer.data)