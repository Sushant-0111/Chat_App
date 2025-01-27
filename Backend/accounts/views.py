from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    
    
    # everything from the front end will be store in data from the request
    # It contain all the information such as Header
    serializer = UserSerializer(data=request.data) 
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors,status=400)
        
        
