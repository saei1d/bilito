from django.shortcuts import render
from rest_framework.response import Response

from client.models import CustomUser


# Create your views here.


def register(request):
    context = {}
    if request.method == 'POST':
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


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('client:home'))
    return render(request, 'login', )
