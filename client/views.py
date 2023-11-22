from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from card.serializers import CustomUserSerializer
from client.models import CustomUser


# Create your views here.

class register(APIView):
    def post(self, request):
        context = {}
        cellphone = request.data.get('cellphone')
        password = request.data.get('password')
        confirm = request.data.get('confirm')
        if CustomUser.objects.filter(cellphone=cellphone).exists():
            context['error_msg'] = 'cellphone has exist!!!'
        else:
            user = CustomUser(cellphone=cellphone)
            if password == confirm:
                user.set_password(password)
                user.save()
                context['msg'] = 'client saved'
            else:
                context['msg'] = "password not  matchable"

        return Response(context)


class Login(APIView):
    def post(self, request):
        context = {}
        cellphone = request.data.get('cellphone')
        password = request.data.get('password')
        user = authenticate(request, cellphone=cellphone, password=password)
        if user:
            login(request, user)
            access_token = str(AccessToken.for_user(user))
            context['access_token'] = access_token
            context['user'] = CustomUserSerializer(user, many=False).data
            context['msg'] = 'Logged in successfully'
            status_code = status.HTTP_200_OK
        else:
            context['msg'] = 'Invalid username or password'
            status_code = status.HTTP_401_UNAUTHORIZED
        return Response(context, status=status_code)

