from django.db import models

class Users():
    username = models.CharField(max_length=20, verbose_name="이름")
    age = models.IntegerField(blank=True, verbose_name="나이")
    userid = models.CharField(max_length=10, verbose_name="아이디")
    password = models.CharField(max_length=50, verbose_name="비밀번호")
    email = models.EmailField(max_length=254, verbose_name="이메일")
    phon_number = models.PhoneNumberField(unique=True)
    register_date = models.DateTimeFieldregister_date = models.DateField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return self.userid


