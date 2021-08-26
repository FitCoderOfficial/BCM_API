from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            users = serializer.save()
            data['response'] = "succssfully registered ad new user"
            data['email'] = users.email
            data['username'] = users.username
        else:
            data = serializer.errors
        return Response(data)