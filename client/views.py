from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from card.serializers import CustomUserSerializer
from client.models import CustomUser
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


# Create your views here.

class Register(APIView):
    permission_classes = (AllowAny,)

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
        print('kjhbgv')
        cellphone = request.data.get('cellphone')
        password = request.data.get('password')
        user = authenticate(cellphone=cellphone, password=password)
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


# @method_decorator(login_required)
class Editprofile(APIView):
    def put(self, request):
        context = {}
        user = CustomUser.objects.get(id=request.user)
        user.cellphone = request.data.get('cellphone' , user.cellphone)
        user.n_code = request.data.get('n_code', user.n_code)
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)


        return Response({'msg': 'profile is update'}, status=status.HTTP_200_OK)
