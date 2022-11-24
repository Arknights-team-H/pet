from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta(AbstractUser.Meta):
        db_table = 'my_user'
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'

    mc_number = models.CharField(max_length=15, verbose_name='個体番号(15桁)')
    user_birthday = models.DateField(verbose_name='ユーザの生年月日')
    pet_id = models.CharField(max_length=11, verbose_name='ペットID')
    pet_name = models.CharField(max_length=40, verbose_name='ペットの名前')
    pet_birthday = models.DateField(verbose_name='ペットの生年月日')


