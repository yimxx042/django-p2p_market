from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
    )

    kakao_id = models.CharField(max_length=20, null=True)

    address = models.CharField(max_length=40, null=True)