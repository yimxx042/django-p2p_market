from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
from django.db import models

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        error_messages={'unique': 'This nickname is already registered.'},
        validators=[validate_no_special_characters],
    )

    kakao_id = models.CharField(
        max_length=20, 
        null=True,
        validators=[validate_no_special_characters],
    )

    address = models.CharField(
        max_length=40, 
        null=True,
        validators=[validate_no_special_characters],
    )