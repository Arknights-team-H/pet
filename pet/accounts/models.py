from django.contrib.auth.models import AbstractUser
from django.db import models

class HospitalUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'

    hospital_id = models.CharField(max_length=7, verbose_name='病院ID')
    hospital_name = models.CharField(max_length=40, verbose_name='病院名')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number = models.CharField(max_length=12, verbose_name='電話番号')
    director_name = models.CharField(max_length=40, verbose_name='責任者名')


