from django.urls import path

from client.views import *

urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('editprofile/',Editprofile.as_view())
]
