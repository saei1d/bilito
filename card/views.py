# from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import BilitSerializers


# Create your views here.

class Flys(APIView):
    def get(self, request):
        context = {}
        q = Q()
        if 'principle' in request.GET:
            if 'purpose' in request.GET:
                b = q & Q(principle=request.GET.get('principle'))
                q = q & Q(purpose=request.GET.get('purpose'))
                mmd = Blit.objects.filter(q, b).order_by(request.GET.get('order_by', '-id').replace('__header', ''))
                context['blit'] = BilitSerializers(mmd, many=True).data
        else:
            context['msg'] = "notfound"
        return Response(context)


class Bilits(APIView):
    def get(self, request, pk):
        context = {}
        try:
            bilit = Blit.objects.get(id=pk)
            context['blite'] = BilitSerializers(bilit, many=False).data
        except:
            context['msg'] = 'bilit not found'
        return Response(context)

