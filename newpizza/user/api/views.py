from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.exceptions import APIException
from django.contrib.auth import logout


''' Exception designed to be rised when User want's to 
    edit account which doesn't belong to him '''

class NotAllowedException(APIException):
    status_code = 403
    default_detail = 'You are not allowed to update this account'
    default_code = 'Not allowed'


''' User registration view '''

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


''' Account update view '''

class UserUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        print(request.user.id, kwargs)
        if request.user.id == int(kwargs['pk']):
            return self.update(request, *args, **kwargs)
        else:
            raise NotAllowedException


''' Login view '''

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validate(serializer.initial_data)
            if user:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_403_FORBIDDEN)
        

''' Logout view '''

class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)



