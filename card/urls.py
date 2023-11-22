from django.urls import path

from card.views import *

urlpatterns = [
    path("", Flys.as_view()),
    path('blits/<int:pk>/', Bilits.as_view()),
]
