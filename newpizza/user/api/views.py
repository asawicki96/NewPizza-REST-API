from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.exceptions import APIException

class NotAllowedException(APIException):
    status_code = 403
    default_detail = 'You are not allowed to update this account'
    default_code = 'Not allowed'

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        if request.user.id == args:
            return self.update(request, *args, **kwargs)
        else:
            error = json.dumps(obj='Not allowed')
            raise NotAllowedException



        


