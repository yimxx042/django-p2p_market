from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from .validators import validate_no_special_characters

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

class Post(models.Model):
    title = models.CharField(max_length=60)
    item_price = models.IntegerField(validators=[MinValueValidator(1)])
    CONDITION_CHOICES = [
        ('NEW', 'NEW'),
        ('BEST', 'BEST'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    item_details = models.TextField(blank=True)

    image1 = models.ImageField(upload_to='item_pics')

    image2 = models.ImageField(upload_to='item_pics', blank=True)

    image3 = models.ImageField(upload_to='item_pics', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title