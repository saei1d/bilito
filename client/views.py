from rest_framework.authentication import BasicAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework_simplejwt.tokens import AccessToken
from card.serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login


# Create your views here.
class Register(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (BasicAuthentication,)

    def post(self, request):
        context = {}
        cellphone = request.data.get('cellphone')
        password = request.data.get('password')
        confirm = request.data.get('confirm')
        if CustomUser.objects.filter(username=cellphone).exists():
            context['error_msg'] = 'cellphone has exist!!!'
        else:
            print(3)
            user = CustomUser(username=cellphone)
            user.cellphone = cellphone
            if password == confirm:
                user.set_password(password)
                user.save()
                context['msg'] = 'client saved'
            else:
                context['msg'] = "password not  matchable"

        return Response(context)


class Login(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (BasicAuthentication,)

    def post(self, request):
        context = {}
        print('kjhbgv')
        cellphone = request.data.get('cellphone')
        password = request.data.get('password')
        user = authenticate(request, username=cellphone, password=password)
        print(user)
        if user:
            login(request, user)
            access_token = str(AccessToken.for_user(user))
            context['access_token'] = access_token
            context['user'] = CustomUserSerializer(user, many=False).data
            context['msg'] = 'Logged in successfully'
            status_code = HTTP_200_OK
        else:
            context['msg'] = 'Invalid username or password'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)


# @method_decorator(login_required)
class Editprofile(APIView):
    authentication_classes = (BasicAuthentication,)

    def put(self, request):
        context = {}
        try:
            user = CustomUser.objects.get(id=request.user)
            user.cellphone = request.data.get('cellphone', user.cellphone)
            user.n_code = request.data.get('n_code', user.n_code)
            user.first_name = request.data.get('first_name', user.first_name)
            user.last_name = request.data.get('last_name', user.last_name)
            context['user'] = CustomUserSerializer(user, many=False).data
            context['msg'] = 'edited successfully'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'Invalid'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)
