from django.db import models

from client.models import CustomUser


class Company(models.Model):
    name = models.CharField(max_length=155)


class Blit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    principle = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    price = models.IntegerField()
    opacity = models.IntegerField(default=0)
    fly_class = models.CharField(max_length=255)
    date = models.DateTimeField()
    deleted = models.BooleanField(default=False)



class MyFlys(models.Model):
    deleted = models.BooleanField(default=False)
    Blit = models.ForeignKey(Blit,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
