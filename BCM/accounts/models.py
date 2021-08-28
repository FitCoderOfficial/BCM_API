from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Users(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    )

    username = models.CharField(max_length=20, verbose_name="이름")
    age = models.IntegerField(blank=True, verbose_name="나이")
    sex = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES, verbose_name="남성 / 여성")
    bio = models.CharField(max_length=255, verbose_name="자기소개")
    userid = models.CharField(max_length=10, verbose_name="아이디")
    password = models.CharField(max_length=50, verbose_name="비밀번호")
    email = models.EmailField(max_length=254, unique=True, verbose_name="이메일")
    phone_number = PhoneNumberField(blank=True, verbose_name="핸드폰 번호")
    register_date = models.DateTimeFieldregister_date = models.DateField(auto_now_add=True, verbose_name='등록일')

    is_active = models.BooleanField(default=True, verbose_name="활성화 / 비활성화")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [username]

    def __str__(self):
        return self.email


