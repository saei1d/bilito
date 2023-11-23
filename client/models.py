from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    cellphone = models.BigIntegerField()
    n_code = models.IntegerField(null=True,blank=True)
    gender = models.BooleanField(default=False)

