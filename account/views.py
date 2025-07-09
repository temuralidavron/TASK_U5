from django.shortcuts import render
from rest_framework import generics

from account.models import User
from account.serializers import UserRegisterSerializer


# Create your views here.


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


