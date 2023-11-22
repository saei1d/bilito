from django.urls import path

from card.views import mmd

urlpatterns = [
    path("", mmd.as_view())
]