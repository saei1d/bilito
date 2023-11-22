from .models import *

from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class BilitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blit
        fields = '__all__'
