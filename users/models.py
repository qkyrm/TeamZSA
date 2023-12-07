from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(User):
    GENDER = (
        ('M', "M"),
        ('Ж', "Ж")
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=18, validators=[MaxValueValidator(26), MinValueValidator(18)])
    gender = models.CharField(max_length=100, choices=GENDER)
