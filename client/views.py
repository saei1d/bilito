from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from client.models import CustomUser


# Create your views here.

class register(APIView):
    def post(self, request):
        context = {}
        cellphone = request.POST.get('cellphone')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
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
        cellphone = request.POST.get('cellphone')
        password = request.POST.get('password')
        user = authenticate(request, cellphone=cellphone, password=password)
        if user:
            login(request, user)

